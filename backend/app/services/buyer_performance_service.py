from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date, datetime, timedelta
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType


def get_buyer_performance(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):
    query = (
        db.query(
            Transaction.party_name.label("buyer_name"),
            func.count(Transaction.id).label("total_sales"),
            func.coalesce(
                func.sum(Transaction.quantity),
                0
            ).label("total_quantity_bought"),
            func.coalesce(
                func.sum(Transaction.revenue),
                0
            ).label("total_revenue"),
            func.coalesce(
                func.sum(Transaction.profit),
                0
            ).label("total_profit"),
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
    # Group By Buyer
    # -----------------------------

    rows = (
        query
        .group_by(Transaction.party_name)
        .order_by(
            func.sum(Transaction.profit).desc()
        )
        .all()
    )

    report = []

    for row in rows:
        report.append({
            "buyer_name": row.buyer_name,
            "total_sales": row.total_sales,
            "total_quantity_bought": Decimal(
                str(row.total_quantity_bought)
            ),
            "total_revenue": Decimal(
                str(row.total_revenue)
            ),
            "total_profit": Decimal(
                str(row.total_profit)
            ),
        })

    return report