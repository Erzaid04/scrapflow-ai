from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.dependencies.roles import require_roles
from app.schemas.report import  ProfitSummaryResponse
from app.routes.auth import get_db
from app.services.report_service import get_profit_summary
router = APIRouter(
    prefix = "/api/v1/reports",
    tags=["Reports"]
)

@router.get("/profit-summary",response_model=ProfitSummaryResponse)
def profit_summary(
    db:Session = Depends(get_db)
):
    return get_profit_summary(db)