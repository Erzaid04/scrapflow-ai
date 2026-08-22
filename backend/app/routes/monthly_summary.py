from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.monthly_summary import MonthlySummary
from app.services.monthly_summary_service import get_monthly_summary


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/monthly-summary",
    response_model=List[MonthlySummary]
)
def monthly_summary(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_monthly_summary(db)
