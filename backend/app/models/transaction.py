from enum import Enum
from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    ForeignKey,
    DateTime,
    Numeric,
    Enum as SqlEnum
)

from sqlalchemy.sql import func

from app.models.base import Base


class TransactionType(str, Enum):
    PURCHASE = "PURCHASE"
    SALE = "SALE"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    transaction_type = Column(
        SqlEnum(TransactionType),
        nullable=False
    )

    inventory_id = Column(
        Integer,
        ForeignKey("inventories.id"),
        nullable=False
    )

    quantity = Column(
        Float,
        nullable=False
    )

    sale_price_per_unit = Column(
        Numeric(10,2),
        nullable=False
    )
    purchase_price_per_unit = Column(Numeric(10,2   ),nullable=False)
    revenue = Column(Numeric(10,2),nullable=False)
    cost = Column(Numeric(10,2),nullable=False)
    profit = Column(Numeric(10,2),nullable=False)
    

    party_name = Column(
        String(255),
        nullable=False
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    inventory = relationship(
        "Inventory"
    )
    
    user = relationship(
        "User"
    )