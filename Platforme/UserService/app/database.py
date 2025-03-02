from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os


url = os.getenv("DATABASE_URL")

engine = create_engine(url)

session_local =  sessionmaker(autocommit = False , autoflush= False , bind=engine)

Base =  declarative_base()