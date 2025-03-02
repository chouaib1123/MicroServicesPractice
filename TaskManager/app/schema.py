from pydantic import BaseModel 
from typing import Optional
import uuid
from enum import Enum

class TaskSchema(BaseModel):
    title : str
    description : str

class ResponseTaskSchema(TaskSchema):
    id : uuid.UUID
    status : str

    class Config: 
        from_attributes  = True

class UpdateTaskSchema(TaskSchema):
    title : Optional[str] = None
    description : Optional[str] = None
    status : Optional[str] = None
