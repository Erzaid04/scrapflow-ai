from pydantic import BaseModel
from decimal import Decimal


class MaterialPerformanceResponse(BaseModel):
    material_name: str
    total_quantity_sold: Decimal
    total_revenue: Decimal
    total_cost: Decimal
    total_profit: Decimal