import uuid
from pydantic import BaseModel


class OrderSchema(BaseModel):
    product_id : uuid.UUID
    quantity : int

class OrderResponseSchema(OrderSchema):
    id : uuid.UUID
    total_amount : float

    class Config:
        from_attributes = True
