from app.Services.OrderService import OrderService
from app.Services.ProductService import ProductService
from app.Configuration.database import session_local
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
def get_order_service(db : Session = Depends(get_db)):
    return OrderService(db)


product_service = Annotated[ProductService , Depends(get_product_service)]
order_Service = Annotated[OrderService , Depends(get_order_service)]