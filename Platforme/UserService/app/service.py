from sqlalchemy.orm import Session
from app.schema import UserSchema , UserResponseSchema


class UserService : 
    def __init__(self , db : Session ):
        self.db = db


    def create_user(self , newuser : UserSchema) -> UserResponseSchema:
        