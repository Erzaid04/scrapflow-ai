from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List
from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.purchase_report import PurchaseReportResponse
from app.services.purchase_report_service import get_purchase_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/purchases",
    response_model=List[PurchaseReportResponse]
)
def purchase_report(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_purchase_report(
        db,
        start_date,
        end_date
    )
    