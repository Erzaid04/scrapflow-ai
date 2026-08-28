from pydantic import BaseModel
from decimal import Decimal
from datetime import date, datetime

from app.models.expense import ExpenseCategory


class ExpenseReportResponse(BaseModel):
    id: int
    category: ExpenseCategory
    amount: Decimal
    description: str | None
    expense_date: date
    created_by: int
    created_at: datetime