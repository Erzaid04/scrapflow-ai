from sqlalchemy.orm import Session
from decimal import Decimal

from app.models.inventory import Inventory


def get_inventory_report(db: Session):

    inventories = db.query(Inventory).all()

    report = []

    for item in inventories:

        inventory_value = (
            Decimal(str(item.quantity))
            * Decimal(str(item.purchase_price_per_unit))
        )

        report.append({
            "id": item.id,
            "material_name": item.material_name,
            "quantity": Decimal(str(item.quantity)),
            "unit": item.unit,
            "purchase_price_per_unit": Decimal(str(item.purchase_price_per_unit)),
            "inventory_value": inventory_value,
            "supplier_name": item.supplier_name,
        })

    return report