from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.auth.jwt_handler import verify_access_token
from app.database.connection import SessionLocal
from app.models.user import User

#Oauth2 dependency
oauth2_schema = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/token"
)

#database dependency
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
def get_current_user(
    token: str = Depends(oauth2_schema),
    db:Session = Depends(get_db)
):
    try:
        payload = verify_access_token(token)
        user_id = payload["sub"]
        user = db.query(User).filter(User.id == user_id).first()
        
        if not user:
            raise HTTPException(
                status_code = 401,
                detail="User not found"
            )
        return user
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )