from sqlalchemy.orm import Session
from datetime import date, datetime, timedelta
from decimal import Decimal

from app.models.transaction import Transaction, TransactionType
from app.models.inventory import Inventory


def get_purchase_report(
    db: Session,
    start_date: date | None = None,
    end_date: date | None = None
):
    query = (
        db.query(Transaction, Inventory)
        .join(
            Inventory,
            Transaction.inventory_id == Inventory.id
        )
        .filter(
            Transaction.transaction_type == TransactionType.PURCHASE
        )
    )

    # -----------------------------
    # Start Date Filter
    # -----------------------------

    if start_date:
        query = query.filter(
            Transaction.created_at >= datetime.combine(
                start_date,
                datetime.min.time()
            )
        )

    # -----------------------------
    # End Date Filter
    # -----------------------------

    if end_date:
        next_day = end_date + timedelta(days=1)

        query = query.filter(
            Transaction.created_at < datetime.combine(
                next_day,
                datetime.min.time()
            )
        )

    transactions = query.order_by(
        Transaction.created_at.desc()
    ).all()

    report = []

    for transaction, inventory in transactions:

        report.append({
            "id": transaction.id,
            "inventory_id": transaction.inventory_id,
            "material_name": inventory.material_name,
            "quantity": Decimal(str(transaction.quantity)),
            "purchase_price_per_unit": Decimal(
                str(transaction.purchase_price_per_unit)
            ),
            "cost": Decimal(str(transaction.cost)),
            "party_name": transaction.party_name,
            "created_by": transaction.created_by,
            "created_at": transaction.created_at,
        })

    return report