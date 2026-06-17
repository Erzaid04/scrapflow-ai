from fastapi import FastAPI,APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.user import UserRegisterSchema
from app.services.user_service import register_user
from app.schemas.user import UserLoginSchema
from app.services.user_service import authenticate_user
from app.auth.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordRequestForm



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
        
@router.post("/login")
def login(
    login_data: UserLoginSchema,
        db: Session = Depends(get_db)
):  
    user = authenticate_user(
        db = db,
        email = login_data.email,
        password=login_data.password
        
    )
    token = create_access_token(
        user_id=user.id,
        role=user.role
    )
    return {
        "access_token":token,
        "token_type":"bearer"
    }
    
@router.post("/token")
def login_for_access_token(
    form_data:OAuth2PasswordRequestForm = Depends(),
    db:Session = Depends(get_db)
):
    user = authenticate_user(
        db =db,
        email = form_data.username,
        password=form_data.password
    )
    token = create_access_token(
        user_id = user.id,
        role = user.role
        
    )
    return {
        "access_token":token,
        "token_type":"bearer"
    }
    