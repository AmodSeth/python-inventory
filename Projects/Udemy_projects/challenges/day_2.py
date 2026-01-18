### bil splitter
# 1. ask the members





total_persons = int(input("How many friends in the group : ")) 
names = []

for i in range(total_persons):
    name = input(f"Enter the name of person {i+1} : ")
    names.append(name)

while True:
    try:
        total_bill = float(input("Enter the total bill amount: "))
        if total_bill < 0 :
            print("Please enter the value greater than 400")
            continue
        break
    except ValueError:
        print("Enter the Correct Value")
    

bill_owed = round(total_bill / total_persons,2)

print("*" * 40)

for name in names:
    print(f"{name} owed {bill_owed}")

print("*" * 40)


    
