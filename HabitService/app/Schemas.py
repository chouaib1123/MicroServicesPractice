from pydantic import BaseModel
import enum
from app.Models import Category
from datetime import date
from typing import Optional
from datetime import date
class FrequancyEnum (str,enum.Enum):
    daily = "daily"
    weekly = "weekly"


class HabitBase(BaseModel):
    name : str
    description : str 
    frequency : FrequancyEnum
    goal : str
    category : int
    start_date : date = date.today()


class HabitCreate(HabitBase):
    pass

class HabitResponse(HabitBase):
    id:int

    class Config:
        from_attributes = True 

class HabbitUpdate(BaseModel):
    name : Optional[str] =  None
    description : Optional[str] =  None
    goal : Optional[str] =  None     


class HabbitsRetrieve(BaseModel):
    name : Optional[str] = None
    description : Optional[str]  = None
    frequency : Optional[FrequancyEnum] = None
    goal : Optional[str] = None
    category : Optional[int] = None
    start_date : Optional[date]    = None
    
    
class ProgressResponse(BaseModel):
    id  : int
    habit_id : int
    date : date
    completed : bool

    class Config:
        from_attributes = True 