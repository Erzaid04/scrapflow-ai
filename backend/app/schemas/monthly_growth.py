from pydantic import BaseModel
from decimal import Decimal


class MonthlyGrowthResponse(BaseModel):
    month: str

    revenue: Decimal
    cost: Decimal
    expenses: Decimal
    profit: Decimal

    revenue_growth_percent: Decimal | None
    profit_growth_percent: Decimal | None