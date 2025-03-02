from passlib.context import CryptContext




Hash_Context = CryptContext(schemes=["bcrypt"])

def HashPassword(password : str) -> str : 
    if password :
        return Hash_Context.hash(password)
    return None


def VerifyPassword(password : str , hpassword : str) -> bool : 
    return Hash_Context.verify(password,hpassword)