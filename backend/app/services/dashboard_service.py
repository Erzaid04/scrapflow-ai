from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal
from datetime import date, datetime, timedelta

from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense
from app.models.inventory import Inventory


def get_dashboard_summary(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):

    # -----------------------------
    # Transaction date filter
    # -----------------------------

    transaction_query = db.query(Transaction)

    if start_date:
        transaction_query = transaction_query.filter(
            Transaction.created_at >= datetime.combine(
                start_date,
                datetime.min.time()
            )
        )

    if end_date:
        next_day = end_date + timedelta(days=1)

        transaction_query = transaction_query.filter(
            Transaction.created_at < datetime.combine(
                next_day,
                datetime.min.time()
            )
        )

    # -----------------------------
    # Revenue
    # -----------------------------

    total_revenue = (
        transaction_query
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
        .with_entities(
            func.coalesce(func.sum(Transaction.revenue), 0)
        )
        .scalar()
    )

    # -----------------------------
    # Cost
    # -----------------------------

    total_cost = (
        transaction_query
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
        .with_entities(
            func.coalesce(func.sum(Transaction.cost), 0)
        )
        .scalar()
    )

    # -----------------------------
    # Expenses
    # -----------------------------

    expense_query = db.query(Expense)

    if start_date:
        expense_query = expense_query.filter(
            Expense.created_at >= datetime.combine(
                start_date,
                datetime.min.time()
            )
        )

    if end_date:
        next_day = end_date + timedelta(days=1)

        expense_query = expense_query.filter(
            Expense.created_at < datetime.combine(
                next_day,
                datetime.min.time()
            )
        )

    total_expenses = (
        expense_query
        .with_entities(
            func.coalesce(func.sum(Expense.amount), 0)
        )
        .scalar()
    )

    # -----------------------------
    # Total Sales
    # -----------------------------

    total_sales = (
        transaction_query
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
        .with_entities(
            func.count(Transaction.id)
        )
        .scalar()
    )

    # -----------------------------
    # Total Purchases
    # -----------------------------

    total_purchases = (
        transaction_query
        .filter(
            Transaction.transaction_type == TransactionType.PURCHASE
        )
        .with_entities(
            func.count(Transaction.id)
        )
        .scalar()
    )

    # -----------------------------
    # Current Inventory Value
    # -----------------------------

    inventory_value = (
        db.query(
            func.coalesce(
                func.sum(
                    Inventory.quantity *
                    Inventory.purchase_price_per_unit
                ),
                0
            )
        )
        .scalar()
    )

    # -----------------------------
    # Net Profit
    # -----------------------------

    net_profit = (
        Decimal(str(total_revenue))
        - Decimal(str(total_cost))
        - Decimal(str(total_expenses))
    )

    return {
        "total_revenue": Decimal(str(total_revenue)),
        "total_cost": Decimal(str(total_cost)),
        "total_expenses": Decimal(str(total_expenses)),
        "net_profit": net_profit,
        "inventory_value": Decimal(str(inventory_value)),
        "total_sales": total_sales,
        "total_purchases": total_purchases,
    }