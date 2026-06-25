from pydantic import BaseModel
from app.models.transaction import TransactionType
from datetime import datetime
class TransactionCreate(BaseModel):
    inventory_id:int
    quantity:float
    price_per_unit:float
    party_name:str
    transaction_type:TransactionType
    
class TransactionResponse(BaseModel):
    id:int
    inventory_id:int
    quantity:float
    price_per_unit:float
    purchase_price_per_unit:float | None = None
    party_name:str
    transaction_type:TransactionType
    created_by:int
    created_at:datetime
    
    class Config:
        form_attributes = True
        
    
    