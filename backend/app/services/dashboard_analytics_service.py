from sqlalchemy.orm import Session
from sqlalchemy import func
from decimal import Decimal
from datetime import date, datetime, timedelta

from app.models.transaction import Transaction, TransactionType
from app.models.expense import Expense
from app.models.inventory import Inventory


def apply_transaction_date_filter(
    query,
    start_date: date | None,
    end_date: date | None
):
    if start_date:
        query = query.filter(
            Transaction.created_at >= datetime.combine(
                start_date,
                datetime.min.time()
            )
        )

    if end_date:
        next_day = end_date + timedelta(days=1)

        query = query.filter(
            Transaction.created_at < datetime.combine(
                next_day,
                datetime.min.time()
            )
        )

    return query


def apply_expense_date_filter(
    query,
    start_date: date | None,
    end_date: date | None
):
    if start_date:
        query = query.filter(
            Expense.expense_date >= start_date
        )

    if end_date:
        query = query.filter(
            Expense.expense_date <= end_date
        )

    return query


def get_dashboard_analytics(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):

    # --------------------------------
    # Financial Overview
    # --------------------------------

    revenue_query = (
        db.query(
            func.coalesce(
                func.sum(Transaction.revenue),
                0
            )
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
    )

    revenue_query = apply_transaction_date_filter(
        revenue_query,
        start_date,
        end_date
    )

    total_revenue = revenue_query.scalar()


    cost_query = (
        db.query(
            func.coalesce(
                func.sum(Transaction.cost),
                0
            )
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
    )

    cost_query = apply_transaction_date_filter(
        cost_query,
        start_date,
        end_date
    )

    total_cost = cost_query.scalar()


    expense_query = (
        db.query(
            func.coalesce(
                func.sum(Expense.amount),
                0
            )
        )
    )

    expense_query = apply_expense_date_filter(
        expense_query,
        start_date,
        end_date
    )

    total_expenses = expense_query.scalar()


    total_revenue = Decimal(str(total_revenue))
    total_cost = Decimal(str(total_cost))
    total_expenses = Decimal(str(total_expenses))

    net_profit = (
        total_revenue
        - total_cost
        - total_expenses
    )


    # --------------------------------
    # Inventory Overview
    # --------------------------------

    inventory_value = (
        db.query(
            func.coalesce(
                func.sum(
                    Inventory.quantity
                    * Inventory.purchase_price_per_unit
                ),
                0
            )
        )
        .scalar()
    )

    inventory_value = Decimal(str(inventory_value))


    total_inventory_items = (
        db.query(
            func.count(Inventory.id)
        )
        .scalar()
    )


    # --------------------------------
    # Top Material
    # --------------------------------

    material_query = (
        db.query(
            Inventory.material_name.label("material_name"),
            func.sum(Transaction.profit).label("profit")
        )
        .join(
            Transaction,
            Transaction.inventory_id == Inventory.id
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
    )

    material_query = apply_transaction_date_filter(
        material_query,
        start_date,
        end_date
    )

    top_material_row = (
        material_query
        .group_by(
            Inventory.material_name
        )
        .order_by(
            func.sum(Transaction.profit).desc()
        )
        .first()
    )


    if top_material_row:
        top_material = top_material_row.material_name
        top_material_profit = Decimal(
            str(top_material_row.profit)
        )
    else:
        top_material = None
        top_material_profit = None


    # --------------------------------
    # Top Buyer
    # --------------------------------

    buyer_query = (
        db.query(
            Transaction.party_name.label("buyer_name"),
            func.sum(Transaction.profit).label("profit")
        )
        .filter(
            Transaction.transaction_type == TransactionType.SALE
        )
    )

    buyer_query = apply_transaction_date_filter(
        buyer_query,
        start_date,
        end_date
    )

    top_buyer_row = (
        buyer_query
        .group_by(
            Transaction.party_name
        )
        .order_by(
            func.sum(Transaction.profit).desc()
        )
        .first()
    )


    if top_buyer_row:
        top_buyer = top_buyer_row.buyer_name
        top_buyer_profit = Decimal(
            str(top_buyer_row.profit)
        )
    else:
        top_buyer = None
        top_buyer_profit = None


    # --------------------------------
    # Top Supplier
    # --------------------------------

    supplier_query = (
        db.query(
            Transaction.party_name.label("supplier_name"),
            func.sum(Transaction.cost).label("cost")
        )
        .filter(
            Transaction.transaction_type == TransactionType.PURCHASE
        )
    )

    supplier_query = apply_transaction_date_filter(
        supplier_query,
        start_date,
        end_date
    )

    top_supplier_row = (
        supplier_query
        .group_by(
            Transaction.party_name
        )
        .order_by(
            func.sum(Transaction.cost).desc()
        )
        .first()
    )


    if top_supplier_row:
        top_supplier = top_supplier_row.supplier_name
        top_supplier_cost = Decimal(
            str(top_supplier_row.cost)
        )
    else:
        top_supplier = None
        top_supplier_cost = None


    # --------------------------------
    # Highest Expense Category
    # --------------------------------

    expense_category_query = (
        db.query(
            Expense.category.label("category"),
            func.sum(Expense.amount).label("amount")
        )
    )

    expense_category_query = apply_expense_date_filter(
        expense_category_query,
        start_date,
        end_date
    )

    top_expense_row = (
        expense_category_query
        .group_by(
            Expense.category
        )
        .order_by(
            func.sum(Expense.amount).desc()
        )
        .first()
    )


    if top_expense_row:
        highest_expense_category = top_expense_row.category
        highest_expense_amount = Decimal(
            str(top_expense_row.amount)
        )
    else:
        highest_expense_category = None
        highest_expense_amount = None


    # --------------------------------
    # Growth
    # --------------------------------

    revenue_growth_percent = None
    profit_growth_percent = None


    # --------------------------------
    # Final Response
    # --------------------------------

    return {
        "total_revenue": total_revenue,
        "total_cost": total_cost,
        "total_expenses": total_expenses,
        "net_profit": net_profit,

        "inventory_value": inventory_value,
        "total_inventory_items": total_inventory_items,

        "top_material": top_material,
        "top_material_profit": top_material_profit,

        "top_buyer": top_buyer,
        "top_buyer_profit": top_buyer_profit,

        "top_supplier": top_supplier,
        "top_supplier_cost": top_supplier_cost,

        "highest_expense_category": highest_expense_category,
        "highest_expense_amount": highest_expense_amount,

        "revenue_growth_percent": revenue_growth_percent,
        "profit_growth_percent": profit_growth_percent,
    }