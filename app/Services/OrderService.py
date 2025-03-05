from colorama import deinit
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.Models.OrderModel import OrderModel
from app.Respositories.OrderRepository import OrderRepository
from app.Respositories.ProductRepository import ProductRepository
from app.Schemas.OrderSchema import OrderSchema, OrderResponseSchema


class OrderService:
    def __init__(self, db: Session):
        self.db = db
        self.product_repo = ProductRepository(db)
        self.order_repo = OrderRepository(db)

    def create_order(self, order: OrderSchema) -> OrderResponseSchema:
        product_existant = self.product_repo.fetch_product_by_id(order.product_id)
        if not product_existant:
            raise HTTPException(status_code=404, detail="product dont exist")

        total_price = product_existant.price * order.quantity
        ready_order = OrderModel(**order.model_dump(), total_amount=total_price)
        added_order = self.order_repo.add_order(ready_order)
        if not added_order :
            raise HTTPException(status_code=500 ,  detail="failed to add Order")

        return OrderResponseSchema.model_validate(added_order)


