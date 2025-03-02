from pydantic import BaseModel , EmailStr
from uuid import UUID

class UserSchema(BaseModel):
    username : str
    email : EmailStr 
    password : str 
    v_password : str



class UserResponseSchema(BaseModel):
    id : UUID
    username : str
    email : str 