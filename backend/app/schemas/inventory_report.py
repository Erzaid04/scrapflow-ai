from pydantic import BaseModel
from decimal import Decimal


class InventoryReportResponse(BaseModel):
    id: int
    material_name: str
    quantity: Decimal
    unit: str
    purchase_price_per_unit: Decimal
    inventory_value: Decimal
    supplier_name: str