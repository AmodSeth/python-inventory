from fastapi import FastAPI, Depends,HTTPException,Path, File, UploadFile
import models
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic_base_model import TodoCreateModel

from Database import engine,session_maker

app = FastAPI()

# this will only run if todos.db exist so when we add something into db 
models.Base.metadata.create_all(bind=engine)

#uvicorn main:app --reload

"""
FastAPI sees yield and understands:
Before yield = setup
After yield = cleanup
"""

def get_db():
    db = session_maker()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def server_health():
    return {"Hello": "World"}


# this is called dependency injection
depends_db = Annotated[Session, Depends(get_db)]
@app.get("/todos")
async def get_todos(db: depends_db):
    # amazonq-ignore-next-line
    todos = db.query(models.Todos).all()
    return {
        "length": len(todos),
        "todos": todos
    }


@app.get("/todos/{todo_id}", status_code=200)
async def get_todo_by_id( db: depends_db, todo_id: int = Path(gt = 0)):
    try:
        todo_by_id = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
        if todo_by_id is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo_by_id
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error occurred")






@app.post("/todos", status_code=201)
async def create_todo(db: depends_db, todo_request: TodoCreateModel):
    todo_model = models.Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    return {"message": "Todo created successfully"}



@app.post("/todos/bulk_upload", status_code=201)
async def create_bulk_todo(file: UploadFile  , db: depends_db ):
    n

    # """
    #     Accepts a CSV file with columns: title, description, priority, is_complete, date_created
    # """
    # if not file.filename:
    #     raise HTTPException(status_code=400, detail="No file uploaded")
    # if not (file.filename.endswith('.csv')):
    #     raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")

    

    
    










