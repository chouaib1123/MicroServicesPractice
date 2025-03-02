from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

DB_URL =  os.getenv("ORDER_DB")

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(autocommit = False , autoflush=False , bind=engine)

Base = declarative_base()