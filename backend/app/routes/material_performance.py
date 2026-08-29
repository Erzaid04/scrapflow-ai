from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.material_performance import MaterialPerformanceResponse
from app.services.material_performance_service import get_material_performance


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/material-performance",
    response_model=List[MaterialPerformanceResponse]
)
def material_performance(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_material_performance(
        db,
        start_date,
        end_date
    )