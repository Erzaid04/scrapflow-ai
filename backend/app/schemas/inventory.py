from pydantic import BaseModel

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