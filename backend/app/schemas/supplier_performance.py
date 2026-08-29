from pydantic import BaseModel
from decimal import Decimal


class SupplierPerformanceResponse(BaseModel):
    supplier_name: str
    total_purchases: int
    total_quantity_purchased: Decimal
    total_cost: Decimal