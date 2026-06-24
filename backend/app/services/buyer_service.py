from sqlalchemy.orm import Session
from app.models.buyer import Buyer
from app.schemas.buyer import BuyerCreate
from fastapi import HTTPException
def create_buyer(
    db:Session,
    buyer_data:BuyerCreate,
    current_user
):    
    exixting_buyer = db.query(
        Buyer
    ).filter(Buyer.phone == buyer_data.phone).first()
    
    if exixting_buyer:
        raise HTTPException(
            status_code = 400,
            detail= "Buyer with this phone number already exists"
            
        )
    
    buyer = Buyer(
        name = buyer_data.name,
        phone = buyer_data.phone,
        adress = buyer_data.address,
        created_by = current_user.id
        
    )
    db.add(buyer)
    db.commit
    db.refresh(buyer)
    return buyer

def get_all_buyers(
    db:Session,
    
):
    buyers=db.query(
        Buyer
        ).all()
    return buyers

def get_buyer_by_id(
    db:Session,
    buyer_id:int
    
):
    buyer = db.query(
        Buyer
    ).filter(Buyer.id == buyer_id).first()
    
    if not buyer:
        raise HTTPException(
            status_code=404,
            detail = "Buyer not found"
        )
    return buyer