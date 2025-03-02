from fastapi import APIRouter
from app import Schemas
from fastapi import Depends,HTTPException,Query
from typing import List,Optional
from app.utils import HabitService
from app.utils import Authenticated


router = APIRouter()


@router.post("/habits/")
def CreateHabbit(service : HabitService ,habit : Schemas.HabitCreate  , Protected : Authenticated):  
        new_habit = service.create_habbit(habit)
        return new_habit

@router.get("/habits/" , response_model=List[Schemas.HabitResponse])
def RetrieveHabbits(service: HabitService, filter: Schemas.HabbitsRetrieve = Depends()):
        habits = service.get_habits(filter)
        return habits

