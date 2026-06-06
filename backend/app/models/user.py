from sqlalchemy import(
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Enum
)
from datetime import datetime
from app.models.base import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key= True,index = True)
    name = Column(String(100),nullable = False)
    email = Column(String(255),unique=True,nullable = False)
    phone_number = Column(String(15),unique = True,nullable = False)
    password_hash = Column(String(255),nullable = False)
    role = Column(Enum("owner","worker","accountant"),default = "owner",nullable = "False")
    is_active = Column(Boolean,default = True)
    created_at = Column(DateTime,default = datetime.utcnow)