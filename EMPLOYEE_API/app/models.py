from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP, UniqueConstraint
from sqlalchemy.sql import func
#sqlalchemy.sql:module for sql functions
#func:used to call database  functions like NOW()
from .database import Base
# .database: means database.py file is in the same folder
# base:is used to create data models

class Employee(Base): 
    __tablename__ = "employees" 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now()) 



    