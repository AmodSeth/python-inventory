from fastapi import FastAPI, Depends,HTTPException,Path, File, UploadFile
import models
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic_base_model import TodoCreateModel

from Database import engine
from routers import auth, notes

app = FastAPI()

# this will only run if todos.db exist so when we add something into db 
models.Base.metadata.create_all(bind=engine)

#include that router
app.include_router(auth.router)
app.include_router(notes.router)


#uvicorn main:app --reload













# @app.post("/todos/bulk_upload", status_code=201)
# async def create_bulk_todo(file: UploadFile  , db: depends_db ):
#     pass
#     # """
#     #     Accepts a CSV file with columns: title, description, priority, is_complete, date_created
#     # """
#     # if not file.filename:
#     #     raise HTTPException(status_code=400, detail="No file uploaded")
#     # if not (file.filename.endswith('.csv')):
#     #     raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    

    
    




    
    
    






