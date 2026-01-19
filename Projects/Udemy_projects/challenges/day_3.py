## Age calculator

def age_calculator(age: int):
    Total_days = age * 365.25 
    Total_hours = 24 * Total_days
    Total_min = 60 * Total_hours

    print(Total_days , Total_hours , Total_min )



def main():
    while Keep_going:
        age = int(input("Enter the age you want to calculate"))
        age_calculator(age)
        print("press q")



main()


