def conditonal_statements():
    friends = ["hola", "amigo","ho"]
    family = ["kaise", "ho"]

    text = input("Enter the name:  ")

    if text in friends:
        print("Hello friend")
    elif text in family:
        print("Hello family")
    else:
        print("fuck off strangers")
    

def while_loops_practise():

    user_input = input("Do you wish to run the program? (yes/no): ")

    while user_input == "yes":
        print("We're running")
        user_input = input("Do you still wish to run the program? (yes/no): ")

    print("we stopped running the loop")


def udemy_practise():
    user_input = input("Enter your input (p/q)")

    while user_input:
        if user_input == "p":
            print("hello")
        if user_input == "q": break
        user_input = input("Enter your input (p/q)")



def for_loops_practise():
    friends = ["hola", "amigo","ho"]
    # for i in friends:
    #     print(i)
    # for i in range(0,10):
    #     print(i)
    for i in range(0,10,2):
        print(i)








if __name__ == "__main__":
    for_loops_practise()