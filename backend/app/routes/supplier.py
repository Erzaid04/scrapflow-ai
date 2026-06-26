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

@router.post("/suppliers",response_model = SupplierResponse)
def create_new_supplier(
    supplier_data:SupplierCreate,
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
@router.get("/suppliers",response_model = list[SupplierResponse])
def get_suppliers(
    db:Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker",
            "accountant"
        )
    )
):
    return get_all_suppliers(db)

@router.get("/suppliers/{supplier_id}",response_model=SupplierResponse)
def supplier_by_id(
    supplier_id:int,
    db:Session = Depends(get_db),
    current_user = Depends(
        require_roles(
            "owner",
            "worker",
            "accountant"
        )
    )
):
    return get_supplier_by_id(db,supplier_id)