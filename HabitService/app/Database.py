from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


Url = os.getenv('DATABASE_URL')


engine = create_engine(Url)


SessionLocal = sessionmaker(autoflush=False , autocommit = False , bind=engine)

Base = declarative_base()




