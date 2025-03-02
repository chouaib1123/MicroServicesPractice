from fastapi import FastAPI
from app.Models import Base
from app.Database import engine
from app.routes import router
app = FastAPI()


@app.on_event("startup")
def iniatDatabase():
    Base.metadata.create_all(bind=engine)

app.include_router(router)