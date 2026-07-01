from sqlalchemy import func
from decimal import Decimal
from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.report import ProfitSummaryResponse

def get_profit_summary(
    db:Session
):
    summary = db.query(
        func.sum(Transaction.revenue).label("total_revenue"),
        func.sum(Transaction.cost).label("total_cost"),
        func.sum(Transaction.profit).label("total_profit")
    ).first()
    return ProfitSummaryResponse(
        total_revenue=summary.total_revenue or Decimal("0.00"),
        total_cost = summary.total_cost or Decimal("0.00"),
        total_profit=summary.total_profit or Decimal("0.00")
    )

