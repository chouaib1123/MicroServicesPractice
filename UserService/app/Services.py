from app.Repositories import userRepository
from sqlalchemy.orm import Session
from app.Schemas import registerSchema,userRespSchema,userSchema
from app.security import HashPassword,VerifyPassword
from app.auth import create_token
from app.Models import UserModel
from fastapi import HTTPException , Response

class userService():
    def __init__(self,db = Session):
         self.db = db
         self.user_repo = userRepository(db)



    def register(self , newuser : registerSchema)->userRespSchema : 
         
        User = self.user_repo.user_existant(newuser.username)

        if not User : 
             if newuser.password == newuser.vpassword :
                  hashedPassword = HashPassword(newuser.password)
                  new_user = UserModel(username = newuser.username , password = hashedPassword)
                  created_user = self.user_repo.create_user(new_user)
                  return userRespSchema.model_validate(created_user)
             else : 
                  raise HTTPException(status_code=400 , detail="passwords are not equal")  
        else :
             raise HTTPException(status_code=400,detail="userAlready Exist")     



    def login(self,user : userSchema , response : Response) -> str :

        User =  self.user_repo.user_existant(user.username)

        if User : 
             if VerifyPassword(user.password,User.password) : 
                token = create_token({"username" : User.username})

                response.set_cookie(
                     key = "Acces-Token",
                     value=token,
                     httponly=True,
                     samesite="lax",
                     secure=False
                )
                return {"token" : token}
             
         
        raise HTTPException(status_code=400 , detail="Verify your credentials")
             
        

        
         
