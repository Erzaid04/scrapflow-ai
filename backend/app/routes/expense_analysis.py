from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.expense_analysis import ExpenseCategoryAnalysisResponse
from app.services.expense_analysis_service import (
    get_expense_category_analysis
)


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/expense-analysis",
    response_model=List[ExpenseCategoryAnalysisResponse]
)
def expense_category_analysis(
    start_date: date | None = None,
    end_date: date | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    require_roles("owner", "accountant")(current_user)

    return get_expense_category_analysis(
        db,
        start_date,
        end_date
    )