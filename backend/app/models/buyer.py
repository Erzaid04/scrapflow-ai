from sqlalchemy.sql import func
from app.models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import  (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey
)

class Buyer(Base):
    __tablename__ ="buyers"
    
    id = Column(Integer,primary_key=True,index = True)
    name = Column(String(100),nullable = False)
    phone = Column(String(10),unique = True,nullable = False)
    address = Column(String(255),nullable=True) 
    created_by = Column(Integer,ForeignKey("users.id"),nullable= False)
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    
    creater = relationship(
        "User"
    )