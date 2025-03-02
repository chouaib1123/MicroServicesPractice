from sqlalchemy import Column , Integer , String , ForeignKey , Enum
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid
import enum

class OrderStatus(str , enum.Enum):
    Pending = "en cours"
    Completed = "complet"
    Cancelled = "annulle"


class OrderModel(Base):
    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True) , default = uuid.uuid4 , primary_key=True , index=True)
    user_id  = Column(UUID(as_uuid=True) , ForeignKey("users.id") , nullable=False)
    product_id  = Column(UUID(as_uuid=True) , ForeignKey("products.id") , nullable=False)
    quantity = Column(Integer , nullable=False)
    status = Column(Enum(OrderStatus) , default=OrderStatus.Pending , nullable=False) 
