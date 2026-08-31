from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.dashboard_analytics import DashboardAnalyticsResponse
from app.services.dashboard_analytics_service import get_dashboard_analytics


router = APIRouter(
    prefix="/api/v1/dashboard",
    tags=["Dashboard"]
)


@router.get(
    "/analytics",
    response_model=DashboardAnalyticsResponse
)
def dashboard_analytics(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_dashboard_analytics(
        db,
        start_date,
        end_date
    )