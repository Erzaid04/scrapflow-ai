from pydantic import BaseModel
from decimal import Decimal


class MonthlySummary(BaseModel):
    month: str
    revenue: Decimal
    cost: Decimal
    expenses: Decimal
    profit: Decimal