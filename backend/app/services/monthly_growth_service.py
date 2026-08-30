from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense


def get_monthly_growth(db: Session):

    # --------------------------------
    # Monthly Sales Data
    # --------------------------------

    sales_rows = (
        db.query(
            func.year(Transaction.created_at).label("year"),
            func.month(Transaction.created_at).label("month"),
            func.coalesce(
                func.sum(Transaction.revenue),
                0
            ).label("revenue"),
            func.coalesce(
                func.sum(Transaction.cost),
                0
            ).label("cost"),
            func.coalesce(
                func.sum(Transaction.profit),
                0
            ).label("gross_profit"),
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
        .group_by(
            func.year(Transaction.created_at),
            func.month(Transaction.created_at)
        )
        .all()
    )

    # --------------------------------
    # Monthly Expenses
    # --------------------------------

    expense_rows = (
        db.query(
            func.year(Expense.expense_date).label("year"),
            func.month(Expense.expense_date).label("month"),
            func.coalesce(
                func.sum(Expense.amount),
                0
            ).label("expenses"),
        )
        .group_by(
            func.year(Expense.expense_date),
            func.month(Expense.expense_date)
        )
        .all()
    )

    monthly_data = {}

    # --------------------------------
    # Add Sales Data
    # --------------------------------

    for row in sales_rows:

        key = f"{int(row.year):04d}-{int(row.month):02d}"

        revenue = Decimal(str(row.revenue))
        cost = Decimal(str(row.cost))

        monthly_data[key] = {
            "month": key,
            "revenue": revenue,
            "cost": cost,
            "expenses": Decimal("0.00"),
            "profit": revenue - cost,
        }

    # --------------------------------
    # Add Expense Data
    # --------------------------------

    for row in expense_rows:

        key = f"{int(row.year):04d}-{int(row.month):02d}"

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

    # --------------------------------
    # Sort Months
    # --------------------------------

    months = sorted(monthly_data.keys())

    result = []

    previous = None

    for month in months:

        current = monthly_data[month]

        revenue_growth = None
        profit_growth = None

        if previous is not None:

            previous_revenue = previous["revenue"]
            previous_profit = previous["profit"]

            # Revenue Growth
            if previous_revenue != 0:
                revenue_growth  = (
                    (
                    current["revenue"] - previous_revenue
                ) / previous_revenue) * Decimal("100").quantize(Decimal("0.01"))

            # Profit Growth
            if previous_profit != 0:
                profit_growth = (
                    (
                        current["profit"]
                        - previous_profit
                    )
                    / abs(previous_profit)
                ) * Decimal("100").quantize(Decimal("0.01"))

        result.append({
    "month": current["month"],
    "revenue": current["revenue"],
    "cost": current["cost"],
    "expenses": current["expenses"],
    "profit": current["profit"],
    "revenue_growth_percent": revenue_growth,
    "profit_growth_percent": profit_growth,
})

        previous = current

    return result