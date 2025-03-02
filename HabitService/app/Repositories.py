from sqlalchemy.orm import Session
from app.Models import Habbit,Category
from fastapi import HTTPException

class HabitRepository :
    def __init__(self , db = Session):
        self.db = db

    def create_habit(self,newhabit : Habbit) -> Habbit:
        self.db.add(newhabit)
        self.db.commit()
        self.db.refresh(newhabit)
        return newhabit
    

    def retrieve_allhabits(self,filters: dict = None) ->Habbit:
        query = self.db.query(Habbit)
        if filters :
            for k,v in filters.items():
                query = query.filter(getattr(Habbit,k) == v)


        return query.all()
        



class CategoryRepository : 
    def __init__(self , db = Session):
        self.db = db

    def retrieve_category(self, id: int) -> Category:
        category = self.db.query(Category).filter(Category.id == id).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category
    
        