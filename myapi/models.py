from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    create_date = Column(DateTime, default=datetime.now)