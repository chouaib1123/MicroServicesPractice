from fastapi import APIRouter,Query
from app.schema import ResponseTaskSchema , TaskSchema , UpdateTaskSchema
from app.utils import task_service
from typing import List
import uuid
router = APIRouter()


@router.post("/task" , response_model = ResponseTaskSchema)
def create_task(newtask : TaskSchema , service : task_service): 
    return service.create_task(newtask)


@router.get("/task/{id}" , response_model=ResponseTaskSchema)
def get_task(id : uuid.UUID , service : task_service):
    return service.get_task_by_id(id)


@router.patch("/task/{id}" , response_model=ResponseTaskSchema)
def update_task(id : uuid.UUID ,task : UpdateTaskSchema, service : task_service):
    return service.update_task_by_id(id,task)


@router.delete("/task/{id}")
def delete_task(id : uuid.UUID , service : task_service):
    return service.delete_task_by_id(id)

@router.get("/tasks" , response_model = List[ResponseTaskSchema])
def get_tasks(service : task_service, offset : int = 0 , limit:int = 10):
    return service.get_task_list(limit=limit , offset=offset)