from pydantic import BaseModel
from decimal import Decimal


class BuyerPerformanceResponse(BaseModel):
    buyer_name: str
    total_sales: int
    total_quantity_bought: Decimal
    total_revenue: Decimal
    total_profit: Decimal