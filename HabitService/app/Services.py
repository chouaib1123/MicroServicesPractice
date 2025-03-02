from datetime import date,timedelta
from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session


from app import Schemas
from app.Repositories import HabitRepository,CategoryRepository
from app.Models import Habbit



class habitService:
    def __init__(self,db: Session):
        self.db = db
        self.habit_repo = HabitRepository(db)
        self.categ_repo = CategoryRepository(db)


    def create_habbit(self ,habit : Schemas.HabitCreate ) -> Schemas.HabitResponse:
        try:
            
            self.categ_repo.retrieve_category(habit.category)

            new_habit = Habbit(**habit.model_dump())

            savedHabit = self.habit_repo.create_habit(new_habit)

            return Schemas.HabitResponse.model_validate(savedHabit)
        
        except HTTPException as e :
            raise e
        except Exception as e :
            raise HTTPException(status_code=400,detail= f"Error : {e}")
        
    def get_habits(self,filter : Schemas.HabbitsRetrieve) -> List[Schemas.HabitResponse]:
        try:
            Filters = filter.model_dump(exclude_none=True,exclude_defaults=True,exclude_unset=True)

            habits = self.habit_repo.retrieve_allhabits(Filters)

            return  [Schemas.HabitResponse.model_validate(habit) for habit in habits]
        
        except Exception as e :
            raise HTTPException(status_code=400,detail= f"Error : {e}")
