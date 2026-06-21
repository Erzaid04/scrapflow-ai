from sqlalchemy.orm import Session
from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate
from app.schemas.inventory import InventoryUpdate

def add_inventory(
    db:Session,
    inventory_data:InventoryCreate,
    user_id:int
):
    inventory = Inventory(
        material_name = inventory_data.material_name,
        quantity = inventory_data.quantity,
        unit = inventory_data.unit,
        purchase_price_per_unit=inventory_data.purchase_price_per_unit,
        supplier_name = inventory_data.supplier_name,
        created_by = user_id
    )
    db.add(inventory)
    db.commit()
    db.refresh(inventory)
    return inventory

def get_all_inventories(db:Session):
    return db.query(Inventory).all()

def get_inventory_by_id(
    db:Session,
    inventory_id:int
):
    inventory =  (
        db.query(Inventory).filter(Inventory.id == inventory_id).first()
    )
    return inventory

def update_inventory(
    db:Session,
    inventory_id:int,
    inventory_data:InventoryUpdate
):
    inventory = get_inventory_by_id(
        db,
        inventory_id
    )
    if inventory is None:
        return None
    
    if inventory_data.material_name is not None:
        inventory.material_name = inventory_data.material_name
    
    if inventory_data.quantity is not None:
            inventory.quantity = inventory_data.quantity
    
    if inventory_data.unit is not None:
            inventory.unit = inventory_data.unit
            
    if inventory_data.purchase_price_per_unit is not None:
            inventory.purchase_price_per_unit = inventory_data.purchase_price_per_unit
    
    if inventory_data.supplier_name is not None:
            inventory.supplier_name = inventory_data.supplier_name
    
    db.commit()
    db.refresh(inventory)
    return inventory

def delete_inventory(
    db:Session,
    inventory_id:int
    
):
    inventory = get_inventory_by_id(
        db,
        inventory_id
    )
    if inventory is None:
        return None
    
    db.delete(inventory)
    
    db.commit()
    
    return True