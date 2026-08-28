from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.models.expense import ExpenseCategory
from app.schemas.expense_report import ExpenseReportResponse
from app.services.expense_report_service import get_expense_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/expenses",
    response_model=List[ExpenseReportResponse]
)
def expense_report(
    start_date: date | None = None,
    end_date: date | None = None,
    category: ExpenseCategory | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_expense_report(
        db,
        start_date,
        end_date,
        category
    )