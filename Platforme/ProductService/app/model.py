from sqlalchemy  import UUID , String , Float, Integer , Column
from app.database import Base
import uuid

class ProductModel(Base):
    __tablename__ =  "products"


    id = Column(UUID(as_uuid=True) , default=uuid.uuid4 , index=True , primary_key=True)
    name  = Column(String(50), nullable=False)
    price = Column(Float , nullable=False)
    stock = Column(Integer , nullable=False)


    
