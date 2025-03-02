from sqlalchemy import Column , Integer , String , Boolean , Date, Enum,ForeignKey
from app.Database import Base
from datetime import datetime
import enum



class FrequancyEnum (str,enum.Enum):
    daily = "daily"
    weekly = "weekly"

class Category(Base):
    __tablename__ = "category"


    id  = Column(Integer , primary_key=True , index=True)
    name = Column(String(255))

class Habbit(Base):
    __tablename__ = "habbits"


    id  = Column(Integer , primary_key=True , index=True)
    name = Column(String(255))
    description = Column(String(255))
    frequency = Column(Enum(FrequancyEnum , name="frequency_enum"))
    goal = Column(String(255))    
    category = Column(Integer, ForeignKey("category.id"))
    start_date = Column(Date,default=datetime.now().date)


class HabbitProgress(Base):
    __tablename__ = "habbitsprogress"

    id  = Column(Integer , primary_key=True , index=True)
    habit_id = Column(Integer, ForeignKey("habbits.id"))
    date = Column(Date , default=datetime.now().date)
    completed = Column(Boolean,default=False)
















