from pydantic import BaseModel,ConfigDict
from typing import Optional
from datetime import datetime
class BuyerCreate(BaseModel):
    
    name:str
    phone:str
    address:str | None = None
    
class BuyerResponse(BaseModel):
    
    id:int
    name:str
    phone:str
    adress:Optional[str] = None
    created_by:int
    created_at:datetime
        
    model_config = ConfigDict(
        from_attributes =True
    )