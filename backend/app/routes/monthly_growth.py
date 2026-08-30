from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.monthly_growth import MonthlyGrowthResponse
from app.services.monthly_growth_service import get_monthly_growth


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/monthly-growth",
    response_model=List[MonthlyGrowthResponse]
)
def monthly_growth(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_monthly_growth(db)