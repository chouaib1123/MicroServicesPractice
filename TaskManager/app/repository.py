from sqlalchemy.orm import Session
from app.model import TaskModel
from fastapi import HTTPException
import uuid
class TaskRespository : 
    def __init__(self , db : Session):
        self.db = db
        
    def add_task(self , newTask : TaskModel):
        self.db.add(newTask)
        self.db.commit()
        self.db.refresh(newTask)
        

    def task_existant(self , field_name , value ):
        return self.db.query(TaskModel).filter(getattr(TaskModel,field_name) == value).first()

    def update_task(self , task : TaskModel , data : dict):
        for key, value in data.items():
            setattr(task, key, value) 

        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self,task : TaskModel):
        self.db.delete(task)
        self.db.commit()

    def get_list_task(self , offset : int , limit : int):
          return self.db.query(TaskModel).offset(offset).limit(limit).all()