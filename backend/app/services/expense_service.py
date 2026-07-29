from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.expense import Expense
from app.schemas.expense import (
    ExpenseCreate,
    ExpenseUpdate,
)


def create_expense(
    expense: ExpenseCreate,
    db: Session,
    current_user: int,
):
    new_expense = Expense(
        category=expense.category,
        amount=expense.amount,
        description=expense.description,
        expense_date=expense.expense_date,
        created_by=current_user,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_all_expenses(db: Session):
    return db.query(Expense).all()


def get_expense_by_id(
    expense_id: int,
    db: Session,
):
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    return expense


def update_expense(
    expense_id: int,
    expense_data: ExpenseUpdate,
    db: Session,
):
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    update_data = expense_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)

    return expense


def delete_expense(
    expense_id: int,
    db: Session,
):
    expense = (
        db.query(Expense)
        .filter(Expense.id == expense_id)
        .first()
    )

    if not expense:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Expense not found",
        )

    db.delete(expense)
    db.commit()

    return {
        "message": "Expense deleted successfully"
    }