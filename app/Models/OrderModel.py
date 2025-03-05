from sqlalchemy import false, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Base import Base
import uuid

class OrderModel(Base):
    __tablename__ = "orders"

    id : Mapped[uuid.UUID] = mapped_column(primary_key=True ,nullable=False , default=uuid.uuid4 )
    product_id :  Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id") , nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    total_amount: Mapped[float] = mapped_column(nullable=False)

    product = relationship("ProductModel" , back_populates="orders")