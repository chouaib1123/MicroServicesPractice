from jose import jwt , JWTError
from passlib.context import CryptContext
from datetime import datetime , timedelta

ALGORITHM = "HS256"
SECRET_KEY = "testtestsecretKey"
LIFETIME = 30

hash_context = CryptContext(schemes=["bcrypt"])

def hash_given_password(password : str) -> str :
    return hash_context.hash(password)

def verify_hash_password(password:str , h_password:str)->bool :
    return hash_context.verify(password,h_password)


def generate_token(data : dict ) -> str : 
    payload = data.copy()
    expire =datetime.utcnow() + timedelta(minutes=LIFETIME)
    payload.update({"exp" : expire })
    return jwt.encode(payload , algorithm= ALGORITHM , key= SECRET_KEY)
    
def get_user(token : str) -> dict :
    try :
        data = jwt.decode(token , algorithm= [ALGORITHM] , key= SECRET_KEY)
        return data
    except JWTError as e :
        return None