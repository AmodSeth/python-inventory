class Student:
    def __init__(self,new_name,new_scores):
        self.name = new_name
        self.score = new_scores

    def average(self):
         return sum(self.score) / len(self.score)


class Garage:
    def __init__(self):
        self.cars = []

    #creating my own len function for this functionality
    def __len__(self):
        return len(self.cars)

    #creating a index
    def __getitem__(self,index):
        return self.cars[index]

    # used to retun a string # using in the debugger
    #always choose the repr coz we can convert str into repr
    def __repr__(self):
        return f"I have {len(self.cars)} cars in my garage"
    

    def __str__(self):
        return f"I have {len(self.cars)} cars in my garage"

    








def oops_basic_1():
    my_student = {
        "name": "John",
        "score": [70,80,90,100]
    }

    average_grade = sum(my_student['score'])/len(my_student['score'])
    print(average_grade)
        




if __name__ == "__main__":
    student_one = Student("Amod Seth", [10,20,30,50])
    print(student_one.average())

    main_garage_1 = Garage()
    main_garage_1.cars.append("Toyota")
    main_garage_1.cars.append("Honda")
    main_garage_1.cars.append("Ford")

    print(len(main_garage_1))
    
    print(Garage.__getitem__(main_garage_1,1))