from app.service import ProductService
from app.database import session_local
from sqlalchemy.orm import Session
from fastapi import Depends
from typing_extensions import Annotated


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


def get_product_service(db : Session = Depends(get_db)):
    return ProductService(db)


product_service = Annotated[ProductService , Depends(get_product_service)]