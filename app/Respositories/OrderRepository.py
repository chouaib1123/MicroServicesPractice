import uuid

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.Models.OrderModel import OrderModel


class OrderRepository:
    def __init__(self , db : Session ):
        self.db = db

    def add_order(self , order : OrderModel):
        try :
            self.db.add(order)
            self.db.commit()
            self.db.refresh(order)
            return order
        except SQLAlchemyError as e :
            return None
