from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, datetime, timedelta
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType
from app.models.inventory import Inventory


def get_material_performance(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):
    query = (
        db.query(
            Inventory.material_name.label("material_name"),
            func.coalesce(
                func.sum(Transaction.quantity),
                0
            ).label("total_quantity_sold"),
            func.coalesce(
                func.sum(Transaction.revenue),
                0
            ).label("total_revenue"),
            func.coalesce(
                func.sum(Transaction.cost),
                0
            ).label("total_cost"),
            func.coalesce(
                func.sum(Transaction.profit),
                0
            ).label("total_profit"),
        )
        .join(
            Inventory,
            Transaction.inventory_id == Inventory.id
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
    )

    # -----------------------------
    # Start Date Filter
    # -----------------------------

    if start_date:
        query = query.filter(
            Transaction.created_at >= datetime.combine(
                start_date,
                datetime.min.time()
            )
        )

    # -----------------------------
    # End Date Filter
    # -----------------------------

    if end_date:
        next_day = end_date + timedelta(days=1)

        query = query.filter(
            Transaction.created_at < datetime.combine(
                next_day,
                datetime.min.time()
            )
        )

    # -----------------------------
    # Group By Material
    # -----------------------------

    rows = (
        query
        .group_by(Inventory.material_name)
        .order_by(
            func.sum(Transaction.profit).desc()
        )
        .all()
    )

    report = []

    for row in rows:
        report.append({
            "material_name": row.material_name,
            "total_quantity_sold": Decimal(
                str(row.total_quantity_sold)
            ),
            "total_revenue": Decimal(
                str(row.total_revenue)
            ),
            "total_cost": Decimal(
                str(row.total_cost)
            ),
            "total_profit": Decimal(
                str(row.total_profit)
            ),
        })

    return report
