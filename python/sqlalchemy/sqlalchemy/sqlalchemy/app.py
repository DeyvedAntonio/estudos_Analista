import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = sqlalchemy.create_engine('sqlite:///users.db', echo=True)

base = declarative_base()

class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    full_name = Column(String(50))
    age = Column(Integer)

base.metadata.create_all(engine)