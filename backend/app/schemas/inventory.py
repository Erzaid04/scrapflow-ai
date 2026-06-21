from pydantic import BaseModel
from typing import Optional
class InventoryCreate(BaseModel):
    material_name:str
    quantity:float
    unit:str
    purchase_price_per_unit:float
    supplier_name:str
    
class InventoryResponse(BaseModel):
    id:int
    material_name:str
    quantity:float
    unit:str
    purchase_price_per_unit:float
    supplier_name:str
    created_by:int
class InventoryUpdate(BaseModel):
    material_name:Optional[str] = None
    quantity:Optional[float] = None
    unit:Optional[str] = None
    purchase_price_per_unit:Optional[float] = None
    supplier_name:Optional[str] = None