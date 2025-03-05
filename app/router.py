from app.utils import product_service
from fastapi import APIRouter
from typing import List
from app.schema import ProductSchema, ProductResponseSchema , ProductUpdateSchema
from uuid import UUID

router = APIRouter()


@router.get("/products" , response_model=List[ProductResponseSchema])
def get_all_products(service : product_service):
    return  service.get_all_products()

@router.get("/products/{id}" , response_model=ProductResponseSchema)
def get_product(service : product_service , product_id : UUID):
    return  service.get_product_by_id(product_id)

@router.post("/products" , response_model=ProductResponseSchema)
def add_product(service : product_service  , product : ProductSchema):
    return  service.create_product(product)

@router.patch("/products/{id}" , response_model=ProductResponseSchema)
def update_product(service : product_service , id : UUID ,product : ProductUpdateSchema):
    return  service.update_product(id,product)

@router.delete("/products/{id}" ,response_model=dict)
def delete_product(service : product_service ,id:UUID  ):
    return  service.delete_product(id)
