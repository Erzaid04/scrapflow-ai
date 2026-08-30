from pydantic import BaseModel
from decimal import Decimal

from app.models.expense import ExpenseCategory


class ExpenseCategoryAnalysisResponse(BaseModel):
    category: ExpenseCategory
    total_expenses: int
    total_amount: Decimal