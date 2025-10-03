from fastapi import FastAPI
from model import Product


app = FastAPI()


@app.get("/")
def greet():
    return "Server is up and running"


@app.get("/greet_2")
def greet_2():
    return "Hello from greet_2"


products = [

   Product(id=1, name="Apple", price=1.0, description="A fruit", quantity=10),
   Product(id=2, name="Orange", price=2.0, description="A fruit", quantity=20),
   Product(id=3, name="Banana", price=3.0, description="A fruit", quantity=30),
   Product(id=4, name="Mango", price=4.0, description="A fruit", quantity=40),  
   Product(id=5, name="Grapes", price=5.0, description="A fruit", quantity=50),


]


@app.get("/products")
def GetAllProducts():
    return products




@app.get('/products/{id}')
def GetProductById(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"


@app.post("/product")
def AddProduct(product: Product):
    products.append(product)
    return product

