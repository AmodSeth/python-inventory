#use to create a location of the database 
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todos.db'

from sqlalchemy import create_engine

engine = create_engine( 
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #only allow 1 thread to access the database
)

#create a local session to the database
from sqlalchemy.orm import sessionmaker

session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declare a base class for our models
from sqlalchemy.ext.declarative import declarative_base
# we will create this and then control the databse
Base = declarative_base()













