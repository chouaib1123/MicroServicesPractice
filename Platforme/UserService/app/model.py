from sqlalchemy import Column , String , Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
import enum

class UserRole(str , enum.Enum):
    ADMIN = "admin"
    CUSTOMER  = "client"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True) , default=uuid.uuid4 , primary_key=True)
    username = Column(String(50) , unique= True , nullable=False )
    email = Column(String(80) , unique= True , nullable=False )
    hashed_password = Column(String(100) , unique= True , nullable=False )   
    role = Column(Enum(UserRole)  , default=UserRole.CUSTOMER )