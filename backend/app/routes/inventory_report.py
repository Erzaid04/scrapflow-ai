from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.inventory_report import InventoryReportResponse
from app.services.inventory_report_service import get_inventory_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/inventory",
    response_model=List[InventoryReportResponse]
)
def inventory_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_inventory_report(db)