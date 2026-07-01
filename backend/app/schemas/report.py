from pydantic import BaseModel
from decimal import Decimal

class ProfitSummaryResponse(BaseModel):
    total_revenue: Decimal
    total_cost: Decimal
    total_profit: Decimal