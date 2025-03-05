from fastapi import APIRouter
from app.Utils.utils import order_Service
from app.Schemas.OrderSchema import OrderResponseSchema , OrderSchema

order_router = APIRouter()

@order_router.post("/order" , response_model=OrderResponseSchema)
def add_order(service :order_Service  , order : OrderSchema):
    return  service.create_order(order)