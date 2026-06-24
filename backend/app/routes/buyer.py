from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles
from app.routes.auth import get_db
from app.schemas.buyer import (
    BuyerCreate,
    BuyerResponse
)
from app.services.buyer_service import (
    create_buyer,
    get_all_buyers,
    get_buyer_by_id
)
router = APIRouter(
    prefix = "/api/v1/buyer",
    tags=["Buyer"]
)


@router.post("/buyers",response_model=BuyerResponse)
def create_new_buyer(
    buyer_data:BuyerCreate,
    db:Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker"
        )
    )
):
    return create_buyer(
        db,
        buyer_data,
        current_user
    )
    
@router.get("/buyers",response_model=list[BuyerResponse])
def get_buyers(
    db:Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker",
            "accountant"
        )
    )
):
    return get_all_buyers(db)

@router.get("/buyers/{buyer_id}",response_model = BuyerResponse)
def get_single_buyer(
    buyer_id:int,
    db:Session=Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker",
            "accountant"
        )
    )
):
    return get_buyer_by_id(
        db,
        buyer_id
    )
    
