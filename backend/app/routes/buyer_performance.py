from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.buyer_performance import BuyerPerformanceResponse
from app.services.buyer_performance_service import get_buyer_performance


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/buyer-performance",
    response_model=List[BuyerPerformanceResponse]
)
def buyer_performance(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_buyer_performance(
        db,
        start_date,
        end_date
    )