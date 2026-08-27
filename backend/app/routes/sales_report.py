from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.sales_report import SalesReportResponse
from app.services.sales_report_service import get_sales_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/sales",
    response_model=List[SalesReportResponse]
)
def sales_report(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_sales_report(
        db,
        start_date,
        end_date
    )