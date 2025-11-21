from pydantic import BaseModel,Field

class TodoCreateModel(BaseModel):
    title: str = Field(min_length=3, max_length=100 , example= "Buy groceries")
    description: str = Field(min_length=5, max_length=300, example= "Milk, Bread, Eggs, and Fruits")
    is_complete: bool
    priority: int = Field(ge=1, le=5, example= 3)
    date_created: str = Field(example= "2024-10-01")
    






