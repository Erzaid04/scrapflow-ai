from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense


def get_monthly_summary(db: Session):

    transaction_rows = (
        db.query(
            extract("year", Transaction.created_at).label("year"),
            extract("month", Transaction.created_at).label("month"),
            func.coalesce(
                func.sum(Transaction.revenue),
                0
            ).label("revenue"),
            func.coalesce(
                func.sum(Transaction.cost),
                0
            ).label("cost"),
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
        .group_by(
            extract("year", Transaction.created_at),
            extract("month", Transaction.created_at)
        )
        .all()
    )

    expense_rows = (
        db.query(
            extract("year", Expense.created_at).label("year"),
            extract("month", Expense.created_at).label("month"),
            func.coalesce(
                func.sum(Expense.amount),
                0
            ).label("expenses"),
        )
        .group_by(
            extract("year", Expense.created_at),
            extract("month", Expense.created_at)
        )
        .all()
    )

    monthly_data = {}

    for row in transaction_rows:
        year = int(row.year)
        month = int(row.month)

        key = f"{year:04d}-{month:02d}"

        monthly_data[key] = {
            "month": key,
            "revenue": Decimal(str(row.revenue)),
            "cost": Decimal(str(row.cost)),
            "expenses": Decimal("0.00"),
            "profit": Decimal(str(row.revenue))
                      - Decimal(str(row.cost)),
        }

    for row in expense_rows:
        year = int(row.year)
        month = int(row.month)

        key = f"{year:04d}-{month:02d}"

        if key not in monthly_data:
            monthly_data[key] = {
                "month": key,
                "revenue": Decimal("0.00"),
                "cost": Decimal("0.00"),
                "expenses": Decimal("0.00"),
                "profit": Decimal("0.00"),
            }

        expenses = Decimal(str(row.expenses))

        monthly_data[key]["expenses"] = expenses

        monthly_data[key]["profit"] = (
            monthly_data[key]["revenue"]
            - monthly_data[key]["cost"]
            - expenses
        )

    return sorted(
        monthly_data.values(),
        key=lambda x: x["month"]
    )