from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class SalesReportResponse(BaseModel):
    id: int
    inventory_id: int
    material_name: str
    quantity: Decimal
    sale_price_per_unit: Decimal
    revenue: Decimal
    cost: Decimal
    profit: Decimal
    party_name: str
    created_by: int
    created_at: datetime