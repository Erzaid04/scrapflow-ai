from datetime import datetime,timedelta 
from jose import jwt
from jose import JWTError 
from dotenv import load_dotenv
import os
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)

def create_access_token(
    user_id:int,
    role:str
):
    expire = datetime.utcnow() + timedelta(
        minutes = ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {
        "sub":str(user_id),
        "role":role,
        "exp":expire
    }                               
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    return token

def verify_access_token(
    token:str
    
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise ValueError("Invalid token")