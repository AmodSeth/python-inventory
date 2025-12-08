from fastapi import FastAPI, Depends,HTTPException,Path, File, UploadFile
import models
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic_base_model import TodoCreateModel
from Database import engine,session_maker
from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError


router = APIRouter()


@router.get("/")
async def server_health():
    return {"Hello": "World"}

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


# this is called dependency injection
depends_db = Annotated[Session, Depends(get_db)]
@router.get("/todos")
async def get_todos(db: depends_db):
    # amazonq-ignore-next-line
    todos = db.query(models.Todos).all()
    return {
        "length": len(todos),
        "todos": todos
    }

@router.get("/todos/{todo_id}", status_code=200)
async def get_todo_by_id( db: depends_db, todo_id: int = Path(gt = 0)):
    try:
        todo_by_id = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    except SQLAlchemyError as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred")

    if todo_by_id is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_by_id
   





@router.post("/todos", status_code=201)
async def create_todo(db: depends_db, todo_request: TodoCreateModel):
    todo_model = models.Todos(**todo_request.model_dump())
    db.add(todo_model)
    db.commit()
    return {"message": "Todo created successfully"}




@router.put("/todo/{todo_id}", status_code=200)
async def update_todo(db: depends_db, todo_request: TodoCreateModel, todo_id: int):
    try:
        #get ht todo from the database
        todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
        if todo_model is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        #update the todo values
        todo_model.title = todo_request.title
        todo_model.description = todo_request.description
        todo_model.priority = todo_request.priority
        todo_model.is_complete = todo_request.is_complete
        todo_model.date_created = todo_request.date_created
        db.commit()
        return {"message": "Todo updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error occurred")


@router.delete("/todo/{todo_id}", status_code=200)
async def delete_todo(db: depends_db, todo_request: TodoCreateModel, todo_id: int = Path(gt = 0)):
    try:
        # find the todo in the database
        todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
        if todo_model is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        db.delete(todo_model)
        db.commit()
        return {"message": "Todo deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Database error occurred in delete request")