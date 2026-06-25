from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles
from app.routes.auth import get_db
from app.schemas.supplier import (
    SupplierCreate,
    SupplierResponse
)
from app.services.supplier_service import (
    create_supplier,
    get_all_suppliers,
    get_supplier_by_id
)

router = APIRouter(
    prefix = "/api/v1/supplier",
    tags=["Supplier"]
)

@router.post("/suppliers",reponse_model = SupplierResponse)
def create_new_supplier(
    supplier_data = SupplierCreate,
    current_user = Depends(
        require_roles(
            "owner",
            "worker"
            
        )
    ),
    db:Session = Depends(get_db)
):
    return create_supplier(
        db,
        supplier_data,
        current_user
    )