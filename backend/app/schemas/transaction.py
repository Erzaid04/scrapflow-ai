from pydantic import BaseModel
from app.models.transaction import TransactionType
from datetime import datetime
from decimal import Decimal
class TransactionCreate(BaseModel):
    transaction_type:TransactionType
    inventory_id:int
    quantity:float
    sale_price_per_unit:Decimal
    party_name:str
    
    
class TransactionResponse(BaseModel):
    transaction_type:TransactionType
    id:int
    inventory_id:int
    quantity:float
    sale_price_per_unit:Decimal
    purchase_price_per_unit:Decimal
    revenue:Decimal
    cost:Decimal
    profit:Decimal
    party_name:str
    
    created_by:int
    created_at:datetime
    
    class Config:
        from_attributes = True
        
    
    