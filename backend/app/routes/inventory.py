from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.dependencies.roles import require_roles
from app.schemas.inventory import InventoryCreate
from app.services.inventory_service import add_inventory
from app.routes.auth import get_db
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