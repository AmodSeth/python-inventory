#we need that base that we got from database

from Database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Todos(Base):
    __tablename__ = "todos"  #name of the table in the database
    id = Column(Integer, primary_key=True, index=True) #primary key is unique for each row
    title = Column(String)
    desciption = Column(String)
    priority = Column(Integer)
    is_complete = Column(Boolean, default=False)
    date_created = Column(String)


    def __init__(self, title: str, description: str, priority: int, is_complete: bool, date_created: str):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_complete = is_complete
        self.date_created = date_created

    
    





