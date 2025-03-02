from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class ProductSchema(BaseModel):
    name : str 
    price : float 
    stock : int

class ProductResponseSchema(ProductSchema):
    id : UUID
    class Config:
        from_attributes = True 

class ProductUpdateSchema(BaseModel):
    name : Optional[str] = None
    price : Optional[float] = None 
    stock : Optional[ int] = None     