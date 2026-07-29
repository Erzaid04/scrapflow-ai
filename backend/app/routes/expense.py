from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.routes.auth import get_db
from app.dependencies.auth import get_current_user
from app.dependencies.roles import require_roles

from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
    ExpenseResponse,
)

from app.services.expense_service import (
    create_expense,
    get_all_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense,
)

router = APIRouter(
    prefix="/api/v1/expense",
    tags=["Expenses"],
)


@router.post(
    "/",
    response_model=ExpenseResponse,
)
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    require_roles("owner", "accountant")(current_user)

    return create_expense(
        expense=expense,
        db=db,
        current_user=current_user.id,
    )


@router.get(
    "/",
    response_model=List[ExpenseResponse],
)
def view_all_expenses(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    require_roles("owner", "accountant")(current_user)

    return get_all_expenses(db)


@router.get(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def view_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    require_roles("owner", "accountant")(current_user)

    return get_expense_by_id(
        expense_id=expense_id,
        db=db,
    )


@router.put(
    "/{expense_id}",
    response_model=ExpenseResponse,
)
def edit_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    require_roles("owner", "accountant")(current_user)

    return update_expense(
        expense_id=expense_id,
        expense_data=expense,
        db=db,
    )


@router.delete(
    "/{expense_id}",
)
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    require_roles("owner", "accountant")(current_user)

    return delete_expense(
        expense_id=expense_id,
        db=db,
    )