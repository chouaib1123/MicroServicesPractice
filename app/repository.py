from app.model import ProductModel
from sqlalchemy.orm import Session
import uuid
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db

    def fetch_all_products(self):
        return self.db.query(ProductModel).all()
    
    def fetch_product_by_id(self, id: uuid.UUID):
        return self.db.query(ProductModel).filter(ProductModel.id == id).first()
    
    def create_product(self, product: ProductModel):
        try:
            self.db.add(product)
            self.db.commit()
            self.db.refresh(product)
            return product
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Database error: {e}")
            return None

    def update_product(self, product: ProductModel, data: dict):
        try:
            for k, v in data.items():
                setattr(product, k, v)
            self.db.commit()
            self.db.refresh(product)
            return product
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Database error: {e}")
            return None
        
    def delete_product(self, product: ProductModel):
        try:
            self.db.delete(product)
            self.db.commit()
            return product
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Database error: {e}")
            return None