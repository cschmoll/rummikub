import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(os.environ['DB_CONNECTION_STRING'])

Session = sessionmaker(bind=engine)