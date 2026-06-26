from sqlalchemy.orm import Session
from app.models.supplier import Supplier
from app.schemas.supplier import SupplierCreate
from fastapi import HTTPException

def create_supplier(
    db:Session,
    supplier_data:SupplierCreate,
    current_user
):
    
    existing_supplier = db.query(Supplier).filter(Supplier.phone == supplier_data.phone).first()
    if existing_supplier:
        raise HTTPException(
            status_code=400,
            detail="Supplier with this phone no is already exists"
        )
    
    supplier = Supplier(
        name = supplier_data.name,
        phone = supplier_data.phone,
        address = supplier_data.address,
        created_by = current_user.id
        
        
    )
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

def get_all_suppliers(
    db:Session
):
    
    suppliers = db.query(Supplier).all()
    return suppliers
        
def get_supplier_by_id(
    db:Session,
    supplier_id:int
):
    supplier_by_id = db.query(Supplier).filter(
        Supplier.id == supplier_id
    ).first()
    
    if not supplier_by_id:
        raise HTTPException(
            status_code= 404,
            detail="Supplier not found"
        )
    return supplier_by_id