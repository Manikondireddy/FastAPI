# database.py : Connect python to postgresql
from sqlalchemy import create_engine
#Sqlalchemy :librarary used to connect python woth database
# Create_engine: function that create connection between python and postgressql
from sqlalchemy.orm import sessionmaker,declarative_base 
# sqlalchemy.orm: (object Relational mapping) ,python class convets to ---->database table,python object convets to database row
DATABASE_URL ="postgresql://postgres:1234@localhost/employee"
#Sessionmaker: is used to create database sessions

engine = create_engine(DATABASE_URL)
#Declarative_base: is used to create database models
SessionLocal= sessionmaker(bind=engine)
Base = declarative_base()
