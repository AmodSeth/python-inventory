from pydantic import BaseModel,Field

class Books:
    Title : str
    Author : str
    Price : float
    category : str


    def __init__(self, Title: str, Author: str, Price: float, category: str):
        self.Title = Title
        self.Author = Author
        self.Price = Price
        self.category = category

    

class BookModel(BaseModel):
    Title : str = Field(min_length=4,max_length=100)
    Author : str = Field(min_length=1, max_length=100)
    Price : float = Field(gt=0 , lt= 10000)
    category : str = Field(min_length=1, max_length=100)

    model_config = {
        "json_schema_extra": {
            "example": {
                "Title": "New Book",
                "Author": "New Author",
                "Price": 150,
                "category": "Fiction"
            }
        }
    }
    
