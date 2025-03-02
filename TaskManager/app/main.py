from fastapi import FastAPI
from sqlalchemy.exc import SQLAlchemyError
from app.database import engine 
from app.model import Base
from app.Controller import router
from app.exception import sqlalchemy_error_handler
app = FastAPI()

@app.on_event("startup")
def InitiateDB():
    Base.metadata.create_all(bind = engine)

app.add_exception_handler(SQLAlchemyError, sqlalchemy_error_handler)
app.include_router(router)