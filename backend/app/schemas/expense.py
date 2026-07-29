from pydantic import BaseModel
from decimal import Decimal
from datetime import date, datetime
from app.models.expense import ExpenseCategory


class ExpenseCreate(BaseModel):
    category: ExpenseCategory
    amount: Decimal
    description: str | None = None
    expense_date: date


class ExpenseUpdate(BaseModel):
    category: ExpenseCategory | None = None
    amount: Decimal | None = None
    description: str | None = None
    expense_date: date | None = None


class ExpenseResponse(BaseModel):
    id: int
    category: ExpenseCategory
    amount: Decimal
    description: str | None
    expense_date: date
    created_by: int
    created_at: datetime

    class Config:
        from_attributes = True