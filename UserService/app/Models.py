from sqlalchemy import Integer,String,Column,DateTime
from app.Database import Base
from datetime import datetime



class UserModel(Base) :
    __tablename__ = "users" 


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime,default=datetime.utcnow())