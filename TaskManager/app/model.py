
from app.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Enum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import enum  
import uuid

class TaskStatus(enum.Enum):  
    PENDING = "a faire"
    RUNNING = "en cours"
    FINISHED = "terminee"


class TaskModel(Base):
    __tablename__ = "task"

    id = Column(UUID(as_uuid=True),unique=True ,default=uuid.uuid4 , index=True , primary_key=True)
    title = Column(String(255),unique=True )
    description = Column(String(255))
    status = Column(Enum(TaskStatus) , default=TaskStatus.PENDING)
    createdAt = Column(DateTime , default=datetime.utcnow)
    updatedAt = Column(DateTime , default=datetime.utcnow , onupdate=datetime.utcnow)