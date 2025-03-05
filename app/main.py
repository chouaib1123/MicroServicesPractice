from fastapi import FastAPI
from app.model import Base
from app.router import router
from app.database import engine

app = FastAPI()

@app.on_event("startup")
def initialize_database():
      Base.metadata.create_all(bind = engine)

app.include_router(router)