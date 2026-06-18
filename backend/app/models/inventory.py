from sqlalchemy import Column,Integer,String,Float,DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from app.models.base import Base

class Inventory(Base):
    __tablename__ ="inventories"
    
    id = Column(Integer,primary_key=True)
    material_name = Column(String(100),nullable = False)
    quantity = Column(Float,nullable = False)
    unit = Column(String(20),nullable = False)
    purchase_price_per_unit = Column(Float,nullable = False)
    supplier_name = Column(String(100),nullable=False)
    created_by = Column(Integer,ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime,server_default=func.now())
    