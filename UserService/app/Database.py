from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os



Url = os.getenv('DATABASE_URL')

engine = create_engine(Url)

SessionLocal = sessionmaker(autoflush=False , autocommit = False , bind=engine)

Base = declarative_base()