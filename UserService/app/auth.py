from jose import jwt,JWTError
from datetime import datetime , timedelta
from fastapi import Request,HTTPException


TOKENLIFETIME = 30
SECREY_KEY = "dqwdqwdqw"



def create_token(data : dict )-> str:
    expire = datetime.utcnow() + timedelta(minutes=TOKENLIFETIME)
    payload = data
    payload.update({"exp" : expire})
    return jwt.encode(payload , SECREY_KEY , algorithm="HS256")


def verify_token(request : Request )->dict:

    token = request.cookies.get("Acces-Token")

    if not token :
        raise HTTPException(status_code=401, detail="No token found")

    try :
        Payload = jwt.decode(token,SECREY_KEY,algorithms="HS256")

        if datetime.utcnow().timestamp() >  Payload["exp"]: 
             raise HTTPException(status_code=401, detail="Invalid token")
        
        return Payload
    except JWTError :
        raise HTTPException(status_code=401, detail="Invalid token")





         

