from app.repository import TaskRespository
from sqlalchemy.orm import Session
from app.schema import TaskSchema , ResponseTaskSchema , UpdateTaskSchema
from fastapi import HTTPException  , status
from app.model import TaskModel
from typing import List
import uuid
class TaskService :
    def __init__(self , db : Session):
        self.db = db
        self.taskrepository = TaskRespository(db)
        


    def create_task(self , newtask : TaskSchema ) -> ResponseTaskSchema :
        task_exists = self.taskrepository.task_existant("title",newtask.title)

        if task_exists :
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= f"task with title {newtask.title}  already exist")
        
        task_added = TaskModel(**newtask.model_dump())

        self.taskrepository.add_task(task_added)

        return ResponseTaskSchema.model_validate(task_added)
    

    def get_task_by_id(self , id : uuid.UUID) -> ResponseTaskSchema :
        task_exists = self.taskrepository.task_existant("id",id)

        if not task_exists : 
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"task with id {id}  doesnt exist")

        return ResponseTaskSchema.model_validate(task_exists)

    def update_task_by_id (self , id : uuid.UUID , newtask : UpdateTaskSchema)-> ResponseTaskSchema : 
        task_exists = self.taskrepository.task_existant("id",id)

        if not task_exists :
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"task with id {id}  doesnt exist")
        
        new_taskdata = newtask.model_dump(exclude_none=True , exclude_unset=True)

        updated_data = self.taskrepository.update_task(task_exists,new_taskdata)

        return ResponseTaskSchema.model_validate(updated_data)
    
    def delete_task_by_id(self, id: uuid.UUID) -> dict:
        task_exists = self.taskrepository.task_existant("id", id)

        if not task_exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Task with ID {id} does not exist"
            )

        self.taskrepository.delete_task(task_exists)  

        return {"message": f"Task with ID {id} has been deleted"}
    
    def get_task_list(self, limit : int , offset : int) -> List[ResponseTaskSchema] :
        tasks = self.taskrepository.get_list_task(offset = offset , limit = limit)
        return [ ResponseTaskSchema.model_validate(task) for  task in tasks ]
