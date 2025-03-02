from fastapi import FastAPI
from app.Database import engine
from app.Models import Base
from app.routes import router
app = FastAPI()

@app.on_event("startup")
def InitiateDB():
    Base.metadata.create_all(bind = engine)



app.include_router(router) 
