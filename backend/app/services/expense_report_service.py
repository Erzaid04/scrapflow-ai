from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta
from decimal import Decimal

from app.models.expense import Expense


def get_expense_report(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None,
    category=None
):
    query = db.query(Expense)

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
    # Category Filter
    # -----------------------------

    if category:
        query = query.filter(
            Expense.category == category
        )

    expenses = query.order_by(
        Expense.expense_date.desc(),
        Expense.created_at.desc()
    ).all()

    report = []

    for expense in expenses:

        report.append({
            "id": expense.id,
            "category": expense.category,
            "amount": Decimal(str(expense.amount)),
            "description": expense.description,
            "expense_date": expense.expense_date,
            "created_by": expense.created_by,
            "created_at": expense.created_at,
        })

    return report