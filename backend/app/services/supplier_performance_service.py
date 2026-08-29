from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, datetime, timedelta
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType


def get_supplier_performance(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):
    query = (
        db.query(
            Transaction.party_name.label("supplier_name"),
            func.count(Transaction.id).label("total_purchases"),
            func.coalesce(
                func.sum(Transaction.quantity),
                0
            ).label("total_quantity_purchased"),
            func.coalesce(
                func.sum(Transaction.cost),
                0
            ).label("total_cost"),
        )
        .filter(
            Transaction.transaction_type == TransactionType.PURCHASE
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
    # Group By Supplier
    # -----------------------------

    rows = (
        query
        .group_by(Transaction.party_name)
        .order_by(
            func.sum(Transaction.cost).desc()
        )
        .all()
    )

    report = []

    for row in rows:
        report.append({
            "supplier_name": row.supplier_name,
            "total_purchases": row.total_purchases,
            "total_quantity_purchased": Decimal(
                str(row.total_quantity_purchased)
            ),
            "total_cost": Decimal(
                str(row.total_cost)
            ),
        })

    return report