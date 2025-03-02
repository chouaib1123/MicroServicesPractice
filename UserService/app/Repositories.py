from sqlalchemy.orm import Session
from app.Models import UserModel



class userRepository() : 
    def __init__(self,db = Session):
        self.db = db


    def create_user(self , user : UserModel) -> UserModel:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user    
    
    def user_existant(self , username : str) -> UserModel:
        return self.db.query(UserModel).filter(UserModel.username == username).first()

    
