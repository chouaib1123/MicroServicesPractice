from app.database import LocalSession
from app.service import TaskService
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from fastapi import Depends

def init_db(): 
  db = LocalSession()
  try :
    yield db 
  finally :
    db.close()


def get_taskService(db : Session = Depends(init_db) ):
    return TaskService(db)


task_service = Annotated[TaskService , Depends(get_taskService)]