from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from decimal import Decimal

from app.models.expense import Expense


def get_expense_category_analysis(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):
    query = (
        db.query(
            Expense.category.label("category"),
            func.count(Expense.id).label("total_expenses"),
            func.coalesce(
                func.sum(Expense.amount),
                0
            ).label("total_amount")
        )
    )

    # -----------------------------
    # Start Date Filter
    # -----------------------------

    if start_date:
        query = query.filter(
            Expense.expense_date >= start_date
        )

    # -----------------------------
    # End Date Filter
    # -----------------------------

    if end_date:
        query = query.filter(
            Expense.expense_date <= end_date
        )

    # -----------------------------
    # Group By Category
    # -----------------------------

    rows = (
        query
        .group_by(Expense.category)
        .order_by(
            func.sum(Expense.amount).desc()
        )
        .all()
    )

    report = []

    for row in rows:
        report.append({
            "category": row.category,
            "total_expenses": row.total_expenses,
            "total_amount": Decimal(
                str(row.total_amount)
            )
        })

    return report