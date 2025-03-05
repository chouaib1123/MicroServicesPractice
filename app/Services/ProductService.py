from app.Models.ProductModel import ProductModel
from app.Schemas.ProductSchema import ProductSchema,ProductResponseSchema,ProductUpdateSchema
from sqlalchemy.orm import Session
from app.Respositories.ProductRepository import ProductRepository
from typing import List
from uuid import UUID
from fastapi import HTTPException , status

class ProductService:
    def __init__(self,db:Session):
        self.db = db
        self.product_repository = ProductRepository(db)

    def get_all_products(self) -> List[ProductResponseSchema]:
        products =  self.product_repository.fetch_all_products()
        return [ProductResponseSchema.model_validate(product) for product in products]
    
    def get_product_by_id(self, id: UUID) -> ProductResponseSchema:
        product =  self.product_repository.fetch_product_by_id(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
        return ProductResponseSchema.model_validate(product)
    
    def create_product(self, product: ProductSchema) -> ProductResponseSchema:
        new_product = ProductModel(**product.model_dump())
        added_product =  self.product_repository.create_product(new_product)
        if not added_product:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create product")
        return ProductResponseSchema.model_validate(added_product)

    def update_product(self, id: UUID, product_data: ProductUpdateSchema) -> ProductResponseSchema:
        product =  self.product_repository.fetch_product_by_id(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
        
        product_data_ready = product_data.model_dump(exclude_none=True, exclude_unset=True)
        update_product =  self.product_repository.update_product(product, product_data_ready)
        if not update_product:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update product")
        return ProductResponseSchema.model_validate(update_product)
    
    def delete_product(self, id:UUID) -> dict:
        product =  self.product_repository.fetch_product_by_id(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")
        
        result =  self.product_repository.delete_product(product)
        if not result:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete product")
        return {"message": f"product with id = {id} has been deleted"}

