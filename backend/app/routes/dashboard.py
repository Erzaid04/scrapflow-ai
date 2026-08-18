from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.dashboard import DashboardResponse
from app.services.dashboard_service import get_dashboard_summary


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/summary",
    response_model=DashboardResponse
)
def dashboard_summary(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_dashboard_summary(
        db,
        start_date,
        end_date
    )