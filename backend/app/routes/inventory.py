from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.dependencies.roles import require_roles
from app.schemas.inventory import InventoryCreate
from app.schemas.inventory import InventoryUpdate
from app.routes.auth import get_db
from app.services.inventory_service import (
    add_inventory,
    get_all_inventories,
    get_inventory_by_id,
    update_inventory,
    delete_inventory)
router = APIRouter(
    prefix = "/api/v1/inventory",
    tags=["Inventory"]
)

@router.post("/")
def create_inventory(
    inventory_data:InventoryCreate,
    current_user=Depends(
        require_roles(
            "owner",
            "worker"
        )
    ),
    db:Session=Depends(get_db)
):
    inventory = add_inventory(
        db = db,
        inventory_data=inventory_data,
        user_id = current_user.id
    )
    return inventory

@router.get("/")
def get_inventory(
    
    current_user = Depends(
        require_roles(
            "owner",
            "worker",
            "accountant"
        )
    ),
    db:Session=Depends(get_db)
):
    inventory = get_all_inventories(db=db)
    return inventory
@router.get("/{inventory_id}")
def get_inventory_by_id_route(
    inventory_id:int,
    current_user = Depends(
        require_roles(
        "owner",
        "worker",
        "accountant"
        )
    ),
    db:Session = Depends(get_db)
):
    inventory = get_inventory_by_id(
        db,
        inventory_id
    )
    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail = "Inventory not found"
        )
    return inventory

@router.put("/{inventory_id}")
def update_inventory_route(
    inventory_id:int,
    inventory_data:InventoryUpdate,
    current_user = Depends(
        require_roles(
            "owner",
            "worker"
        )
    ),
    db:Session = Depends(get_db)
):
    inventory = update_inventory(
        db,
        inventory_id,
        inventory_data
    )
    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )
    return {
        "message":"Inventory updated successfully"
    }

@router.delete("/{inventory_id}")
def delete_inventory_route(
    
    inventory_id:int,
    current_user = Depends(
        require_roles(
            "owner"
            )
        ),
    db:Session = Depends(get_db),
):
    deleted = delete_inventory(
        db,
        inventory_id
    )
    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Inventory not found"
        )
        
    return {
        "message":"Inventory deleted successfully"
    }
    