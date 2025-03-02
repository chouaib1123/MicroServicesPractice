from sqlalchemy.orm import Session
from fastapi import Depends,Request,HTTPException
from jose import jwt,JWTError
from app.Services import habitService
from app.Database import SessionLocal
from typing_extensions import Annotated
from datetime import datetime

SECREY_KEY = "dqwdqwdqw"

def get_db():
    db = SessionLocal()
    try :
        yield db 
    finally:
        db.close()    

def get_Habit_Service (db: Session = Depends(get_db)) -> habitService:
    return habitService(db)

def verify_token(request : Request )->dict:

    token = request.cookies.get("Acces-Token")

    if not token :
        raise HTTPException(status_code=401, detail="No token found")

    try :
        Payload = jwt.decode(token,SECREY_KEY,algorithms="HS256")

        if datetime.utcnow().timestamp() >  Payload["exp"]: 
             raise HTTPException(status_code=401, detail="Invalid token")
        print(f"Decoded token payload: {Payload}")

        return Payload["username"]
    except JWTError :
        raise HTTPException(status_code=401, detail="Invalid token")

def get_User(request : Request):
    return verify_token(request)

HabitService = Annotated[habitService, Depends(get_Habit_Service)]
Authenticated = Annotated[dict , Depends(get_User)]

