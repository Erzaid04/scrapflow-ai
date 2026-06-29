from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
class InventoryCreate(BaseModel):
    material_name:str
    quantity:Decimal
    unit:str
    purchase_price_per_unit:Decimal
    supplier_name:str
    
class InventoryResponse(BaseModel):
    id:int
    material_name:str
    quantity:Decimal
    unit:str
    purchase_price_per_unit:Decimal
    supplier_name:str
    created_by:int
class InventoryUpdate(BaseModel):
    material_name:Optional[str] = None
    quantity:Optional[Decimal] = None
    unit:Optional[str] = None
    purchase_price_per_unit:Optional[Decimal] = None
    supplier_name:Optional[str] = None