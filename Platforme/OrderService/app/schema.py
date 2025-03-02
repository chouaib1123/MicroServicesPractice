from pydantic import BaseModel
import uuid
import enum

class OrderStatus(str , enum.Enum):
    Pending = "en cours"
    Completed = "complet"
    Cancelled = "annulle"



class OrderSchema(BaseModel):
    user_id : uuid.UUID
    product_id : uuid.UUID
    quantity : int
    status : OrderStatus


class ResponseSchema(OrderSchema):
    id : uuid.UUID

    class Config:
        from_attributes = True
