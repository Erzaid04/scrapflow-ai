from fastapi import FastAPI,APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user import UserRegisterSchema
from app.services.user_service import register_user


app = FastAPI()
router = APIRouter(
    prefix = "/api/v1/auth",
    tags = ["Authentication"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user_data:UserRegisterSchema,db:Session = Depends(get_db)):
        user = register_user(db=db,user_data = user_data)
        return {
            "success":True,
            "message":"User registered successfully",
            "user":{
                "id":user.id,
                "name":user.name,
                "email":user.email,
                "phone_number":user.phone_number,
                "role":user.role
            }
        }