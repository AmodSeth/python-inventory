from fastapi import FastAPI,Body
from models.Books import Books,BookModel


app = FastAPI()

Books_in_store = [
    Books(Title="Book One", Author="Author One", Price=100, category="Science"),
    Books(Title="Book Two", Author="Author Two", Price=200, category="Maths"),
    Books(Title="Book Three", Author="Author Three", Price=300, category="History")
]

@app.get("/")
def server_health_check():
    return {
        "status_code": "200",
        "message": "Server is healthy"
    }

@app.get("/books")
def get_all_books():
    return {
        "status_code": "200",
        "data": Books_in_store
    }

# @app.post("/create_book")
# def app_books(request_body=Body()):
#     Books_in_store.append(request_body)
#     return {
#         "status_code": "200",
#         "data": Books_in_store
#     }



@app.post("/create_book")
def create_book_from_pydantic(book_request: BookModel):
    """
    book_request.model_dump() - Converts the Pydantic BookModel object into a Python dictionary
    Example: {"Title": "New Book", "Author": "New Author", "Price": 150, "category": "Fiction"}

    Books(**dict) - Uses dictionary unpacking to pass the values as keyword arguments to the Books constructor
    now **model dump is used tionary into separate keyword arguments

    Equivalent to: Books(Title="New Book", Author="New Author", Price=150, category="Fiction")
    """
    new_book = Books(**book_request.model_dump())
    Books_in_store.append(new_book)
    return {
        "status_code": "200",
        "data": Books_in_store
    }
   



@app.get("/get_book_by_price/{price}")
async def get_book_by_price(price: int):
   
    for book in Books_in_store:
        if book.Price == price:
            return book
    return None


@app.get("/get_book_by_author/{author}")
async def get_book_by_author(author: str):
    for book in Books_in_store:
        if book.Author.casefold() == author.casefold():
            return book
    return None

@app.get("/find_book_index_by_title/{title}")
async def find_book_index_by_title(title: str):
    for i, book in enumerate(Books_in_store):
        if book.Title.casefold() == title.casefold():
            return i
    return -1


