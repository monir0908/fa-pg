from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.types import Date
from database import Base

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True, index=True)    
    first_name = Column(String(255))
    last_name = Column(String(255))
    password = Column(String(255))
    mobile = Column(String(255))
    email = Column(String(255))
    created_date = Column(Date)

