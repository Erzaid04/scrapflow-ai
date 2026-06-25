from sqlalchemy.orm import Session
from app.models.transaction import Transaction, TransactionType
from app.models.inventory import Inventory
from fastapi import HTTPException, status

def validate_inventory_exists(
    db:Session,
    inventory_id:int
):
    inventory = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if not inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Inventory with id {inventory_id} not found"
        )
    return inventory


def update_invnetory_for_transaction(
    inventory:Inventory,
    transaction_data
):
    if transaction_data.transaction_type == TransactionType.PURCHASE:
        inventory.quantity += transaction_data.quantity
    elif transaction_data.transaction_type == TransactionType.SALE:
        if inventory.quantity < transaction_data.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Not enough quantity in inventory to complete the sale"
            )
        inventory.quantity -= transaction_data.quantity
        
        
def create_transaction(
    db:Session,
    transaction_data,
    current_user_id:int
):
    inventory = validate_inventory_exists(
        db,
        transaction_data.inventory_id
    )
    if transaction_data.transaction_type == TransactionType.SALE:
        purchase_price_snapshot = inventory.purchase_price_per_unit
    else:
        purchase_price_snapshot = None
    update_invnetory_for_transaction(
        inventory,
        transaction_data
        
    )
    transaction = Transaction(
        transaction_type=transaction_data.transaction_type,
        inventory_id=transaction_data.inventory_id,
        quantity=transaction_data.quantity,
        price_per_unit=transaction_data.price_per_unit,
        purchase_price_per_unit = purchase_price_snapshot,
        party_name=transaction_data.party_name,
        created_by=current_user_id
    )
    
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    
    return transaction