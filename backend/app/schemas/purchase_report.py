from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime


class PurchaseReportResponse(BaseModel):
    id: int
    inventory_id: int
    material_name: str
    quantity: Decimal
    purchase_price_per_unit: Decimal
    cost: Decimal
    party_name: str
    created_by: int
    created_at: datetime