from pydantic import BaseModel,ConfigDict
from datetime import datetime
class SupplierCreate(BaseModel):
    name:str
    phone:str
    address:str
class SupplierResponse(BaseModel):
    id:int
    name:str
    phone:str
    address:str
    created_by:int
    created_at:datetime
    
    model_config = ConfigDict(from_attributes=True)