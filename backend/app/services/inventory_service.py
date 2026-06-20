from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate

def add_inventory(
    db:Session,
    inventory_data:InventoryCreate,
    user_id:int
):
    inventory = Inventory(
        material_name = inventory_data.material_name,
        quantity = inventory_data.quantity,
        unit = inventory_data.unit,
        supplier_name = inventory_data.supplier_name,
        created_by = user_id
    )
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory