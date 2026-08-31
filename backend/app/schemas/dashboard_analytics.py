from pydantic import BaseModel
from decimal import Decimal


class DashboardAnalyticsResponse(BaseModel):
    # Financial Overview
    total_revenue: Decimal
    total_cost: Decimal
    total_expenses: Decimal
    net_profit: Decimal

    # Inventory
    inventory_value: Decimal
    total_inventory_items: int

    # Top Performance
    top_material: str | None
    top_material_profit: Decimal | None

    top_buyer: str | None
    top_buyer_profit: Decimal | None

    top_supplier: str | None
    top_supplier_cost: Decimal | None

    highest_expense_category: str | None
    highest_expense_amount: Decimal | None

    # Growth
    revenue_growth_percent: Decimal | None
    profit_growth_percent: Decimal | None