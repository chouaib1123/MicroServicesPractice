from app.Database import SessionLocal
from app.Services import userService
from sqlalchemy.orm import Session
from fastapi import Depends
from typing_extensions import Annotated

def get_db():
    db = SessionLocal()
    try :
        yield db 
    finally:
        db.close()    


def get_UserService(db : Session = Depends(get_db) ) ->userService:
    return userService(db)


user_Service = Annotated[userService,Depends(get_UserService)]    