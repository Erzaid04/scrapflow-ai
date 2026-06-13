from pydantic import BaseModel,EmailStr,Field 
import re

class UserRegisterSchema(BaseModel):
    name:str = Field(...,min_length=2,max_length=100)
    email:EmailStr
    phone_number:str = Field(...,min_length=10,max_length=10)
    password:str = Field(...,min_length=8)
    