from fastapi import FastAPI

app = FastAPI()
from app.routes.auth import router as auth_router
from app.routes.users import router as users_router
from app.routes.inventory import router as inventory_router
from app.routes.transaction import router as transaction_router
from app.routes.buyer import router as buyer_router
from app.routes.expense import router as expense_router
from app.routes.supplier import router as supplier_router
from app.routes.dashboard import router as dashboard_router
from app.routes.monthly_summary import router as monthly_summary_router
app.include_router(monthly_summary_router)
app.include_router(dashboard_router)
app.include_router(supplier_router)
app.include_router(expense_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(inventory_router)
app.include_router(transaction_router)
app.include_router(buyer_router)

@app.get("/")
def root():
    return {"message": "ScrapFlow AI API Running"}
