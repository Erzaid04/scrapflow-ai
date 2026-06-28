from sqlalchemy.orm import Session
from app.models.transaction import Transaction, TransactionType
from app.models.inventory import Inventory
from app.schemas.transaction import TransactionCreate
from fastapi import HTTPException, status
from decimal import Decimal

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


def update_inventory_for_transaction(
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
    db: Session,
    transaction_data: TransactionCreate,
    current_user
):
    if transaction_data.transaction_type == TransactionType.PURCHASE:
        return create_purchase_transaction(
            db,
            transaction_data,
            current_user
        )

    return create_sale_transaction(
        db,
        transaction_data,
        current_user
    )
def create_purchase_transaction(
    db:Session,
    transaction_data:TransactionCreate,
    current_user
):
    inventory = validate_inventory_exists(
        db,
        transaction_data.inventory_id
        
    )
    cost = (
        transaction_data.quantity * 
        inventory.purchase_price_per_unit
    )
    revenue = Decimal("0.00")
    profit = Decimal("0.00")
    sale_price_per_unit = Decimal("0.00")
    
    transaction = Transaction(
        transaction_type = transaction_data.transaction_type,
        inventory_id=inventory.id,
        quantity = transaction_data.quantity,
        sale_price_per_unit=sale_price_per_unit,
        purchase_price_per_unit = inventory.purchase_price_per_unit,
        revenue=revenue,
        cost = cost,
        profit=profit,
        
        party_name = transaction_data.party_name,
        created_by = current_user.id
        )
    db.add(transaction)
    inventory.quantity+=transaction_data.quantity
    db.commit()
    db.refresh(transaction)
    return transaction

def create_sale_transaction(
    db:Session,
    transaction_data:TransactionCreate,
    current_user
):
    
    inventory = validate_inventory_exists(
        db,
        transaction_data.inventory_id
        
    )
    if inventory.quantity < transaction_data.quantity:
        raise HTTPException(
            status_code=400,
            detail="Insuifficient inventory"
            
        )
    purchase_price_snapshot = inventory.purchase_price_per_unit
    revenue = (transaction_data.quantity * transaction_data.sale_price_per_unit)
    cost = (transaction_data.quantity * purchase_price_snapshot)
    profit = revenue - cost

    transaction = Transaction(
                transaction_type = transaction_data.transaction_type,
                inventory_id=inventory.id,
                quantity = transaction_data.quantity,
                sale_price_per_unit=transaction_data.sale_price_per_unit,
                purchase_price_per_unit = purchase_price_snapshot,
                revenue=revenue,
                cost = cost,
                profit=profit,
                
                party_name = transaction_data.party_name,
                created_by = current_user.id
    )
    db.add(transaction)
    inventory.quantity-=transaction_data.quantity
    db.commit()
    db.refresh(transaction)
    return transaction
