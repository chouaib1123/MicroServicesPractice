from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


url = "postgresql+psycopg2://postgres:chouaib@localhost/test"

engine = create_engine(url)

session_local =  sessionmaker(autocommit = False , autoflush= False , bind=engine)

Base =  declarative_base()