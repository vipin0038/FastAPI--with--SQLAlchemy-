from sqlalchemy import Column,Integer,String
from database import Base


# create user date in mysql database
class Users(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))
    password = Column(String(100))


