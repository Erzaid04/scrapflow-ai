from fastapi import APIRouter, Depends
from app.routes.auth import get_db
from sqlalchemy.orm import Session
from app.schemas.transaction import (TransactionCreate, TransactionResponse)
from app.services.transaction_service import create_transaction
from app.dependencies.roles import get_current_user
from app.dependencies.roles import require_roles


router = APIRouter(
    prefix = "/api/v1/transaction",
    tags=["Transaction"]
)

@router.post("/transactions",response_model = TransactionResponse)
def create_new_transaction(
    transaction_data:TransactionCreate,
    db:Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker"
        ))
    
    
):
    return create_transaction(
        db,
        transaction_data,
        current_user
    )
    