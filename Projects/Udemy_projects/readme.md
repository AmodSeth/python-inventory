### Virtual enviornment
pip is a python packet manager 
command to create a new project
``` bash
python3 -m venv first_project
source first_project/bin/activate


pip list # to check the installed packages
```

### Installing packages for fast api
``` bash
pip install fastapi
pip install "uvicorn[standard]"
```

### to start the server
```bash
fastapi dev Books.py 
```

### Project overview
[] will be creating a books inventory project
[] CRUD opeations
[] Books structure  
Books = {
    { "Title" : "Title One" , "Author" : "Author One", "Category" : "Category One"  },
    { "Title" : "Title Two" , "Author" : "Author Two", "Category" : "Category Two"  },
    { "Title" : "Title Three" , "Author" : "Author Three", "Category" : "Category Three"  },
}

[] Read -- > Get
[] Create --> Post
[] Update --> Put
[] Delete --> Delete

### query parameter