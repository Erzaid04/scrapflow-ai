from pydantic import BaseModel
from decimal import Decimal


class DashboardResponse(BaseModel):
    total_revenue: Decimal
    total_cost: Decimal
    total_expenses: Decimal
    net_profit: Decimal
    inventory_value: Decimal
    total_sales: int
    total_purchases: int