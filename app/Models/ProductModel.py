from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from .Base import Base
import uuid


class ProductModel(Base):
        __tablename__ =  "products"

        id : Mapped[uuid.UUID] = mapped_column(default=uuid.uuid4 , primary_key=True)
        name : Mapped[str] = mapped_column(nullable=False)
        price : Mapped[float] = mapped_column(nullable=False)
        stock : Mapped[int] = mapped_column(nullable=False)

        orders = relationship("OrderModel", back_populates="product")
