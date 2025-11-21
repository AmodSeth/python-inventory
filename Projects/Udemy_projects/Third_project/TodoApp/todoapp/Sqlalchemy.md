### SQLAlchemy is basically referred to as the toolkit of Python SQL that provides developers with the flexibility of using the SQL database. The benefit of using this particular library is to allow Python developers to work with the language's own objects, and not write separate SQL queries. They can basically use Python to access and work with databases. 
### SQLAlchemy is also an Object Relational Mapper which is a technique used to convert data between databases or OOP languages such as Python.

### to install SQLAlchemy
``` 
pip install sqlalchemy
```




``` bash
Short Writeup: SQLAlchemy Database Configuration
Your Database.py file sets up the foundation for a SQLAlchemy-based database connection in a FastAPI/web application. Here's what each part does:

Database URL Configuration:

Uses SQLite database stored in todos.db file
The ./ prefix means it's created in your current directory
Engine Creation:
create_engine() establishes the database connection
check_same_thread: False allows multiple threads to access SQLite (needed for web apps)
Session Management:
SessionMaker creates database sessions for transactions
autocommit=False means you control when changes are saved
autoflush=False gives you manual control over when data is sent to the database
Base Class:
declarative_base() creates a base class for your database models
All your table models will inherit from this Base class
```

### model structure

id: --> int (Primary Key) 
title --> str
discription --> str
priority --> int (1---5)
is_complete --> bool (True/False)
date_created --> datetime


### Sqllite Commands
```bash
# To create a new SQLite database file
sqlite3 todos.db
# To open an existing SQLite database file
sqlite3 todos.db
# To list all tables in the database
.tables
# To view the schema of a specific table
.schema table_name

# to view in column mode
.mode column
.mode box
.mode markdown
.mode table 

# exit the SQLite prompt
.exit



## insert commands
code ``` sql
INSERT INTO todos (title, desciption, priority, is_complete, date_created)
VALUES ('Buy milk', 'Get skimmed milk', 1, 0, datetime('now', 'localtime'));
```

### datetime writeup
⏳ SQLite Date & Time Quick Guide

SQLite provides built-in functions to insert the current date/time without needing Python or external code.

1. Current Date & Time (UTC)
datetime('now')


Example:

INSERT INTO todos (date_created) VALUES (datetime('now'));


Output format: YYYY-MM-DD HH:MM:SS

2. Current Date & Time (Local Time)
datetime('now', 'localtime')


Example:

INSERT INTO todos (date_created) VALUES (datetime('now', 'localtime'));

3. Current Date Only
date('now')


Example:

INSERT INTO todos (date_created) VALUES (date('now'));


Output: YYYY-MM-DD

4. Current Time Only
time('now')

Example:
INSERT INTO todos (date_created) VALUES (time('now'));
Output: HH:MM:SS
5. Automatic Timestamp (Recommended)
Set a column to automatically store timestamp on insert:
date_created TEXT DEFAULT (datetime('now'))
Then you can skip date_created in INSERT.


```
Request arrives
 ↓
get_db() starts
 ↓
db = session_maker()
 ↓
yield db → give to endpoint
 ↓
Endpoint uses db
 ↓
Endpoint finishes
 ↓
Cleanup runs (finally)
 ↓
db.close()

```






