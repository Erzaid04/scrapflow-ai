from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    Numeric,
    Enum,
    Date,
)
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.models.base import Base


class ExpenseCategory(enum.Enum):
    ELECTRICITY = "ELECTRICITY"
    TRANSPORT = "TRANSPORT"
    SALARY = "SALARY"
    RENT = "RENT"
    MAINTENANCE = "MAINTENANCE"
    OTHER = "OTHER"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    category = Column(
        Enum(ExpenseCategory),
        nullable=False
    )

    amount = Column(
        Numeric(18, 2),
        nullable=False
    )

    description = Column(
        String(255),
        nullable=True
    )

    expense_date = Column(
        Date,
        nullable=False
    )

    created_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # Relationships
    user = relationship("User", back_populates="expenses")