from sqlalchemy import (
    Column,
    String,
    Float,
    Integer,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy import func
from app.models.base import Base

class Supplier(Base):
    
    __tablename__ = "suppliers"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    phone = Column(String(15),unique=True,nullable=False)
    address = Column(String(100),nullable=False)
    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    creator = relationship("User")
    transactions = relationship(
    "Transaction",
    back_populates="supplier"
)