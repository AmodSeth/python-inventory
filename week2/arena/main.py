from Enemy import *
from Zombie import *
from Ogre import *





def battle(e : Enemy):
    e.talk()
    e.attack()

    e.special_attack()




ogre1 = Ogre(20,5)
zombie1 = Zombie(15,3)

battle(ogre1)
battle(zombie1)







"""
Abstraction: we use the functionality of the Enemy class without knowing what it is
for eg: if my class has a function name talk
we don't care what talk function does internally , we just call it directly

## usecases : 
uses to create the simple and reusable code
DRY principle works the best for it
"""


"""
Constructors:
are used to create objects of a class with or without starting values
Type: 
default and Empty contructor
No arguments
Constructor with arguments

"""


"""
Encapsulation: Bundling of data
we want the attributes not to change once the object is created

we can do it by using __ (double underscore) methods in python
it makes it private and we can access it only through the methods
    its called getters and setters method

usecases:
Helps keeps related data together
Makes code cleaner and easire to read
provides more resuablity with out code

"""

"""
    Self vs Super
    self: refers to the current object
    super: refers to the parent class

    class Person:
        def __init__(self, name,age):
            self.name = name
            self.age = age


    class Student(Person):
        def __init__(self, name,age,student_id):

            #super().__init__(name=name,age=age)
            #super().__init__(self,name,age)
            self.student_id = student_id
            self.subjects = []

"""