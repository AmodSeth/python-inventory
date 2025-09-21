def dictionaries_practise():

    friends = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
    }

    for name , age  in friends.items():
        print(name , age )



def fizz_buzz():

    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
            continue
        if i % 5 == 0:
            print("Buzz")
            continue
        if i % 3 == 0:
            print("Fizz")
            continue
        else:
            print(i)
        
### important ###
def for_with_else_loop_practise():
    cars = ["ok", "ok","ok","ok","ok","ok","ok","faulty"]

    for status in cars:
        if status == "faulty":
            print(f"stopping the production line: {status}")
            break #remove break to keep the else running
        print(f"The car production is fine: {status}")
    else:
        print("The car production is Completed")

def find_prime_number ():
    #divisble by itself and 1
    # for i in range(1, i):
        
    pass


def list_slicing():
    numbers = [0,1,2,3,4,5,6,7]
    doubled_number = []
    #[operation i want to perform >> then the iteration of for loop]
    doubled_number = [ number * 2 for number in numbers]
    print(doubled_number)

    subtracted_numbers = [ i - 1 for i in numbers]

    print(subtracted_numbers)

    #creating multiple strings

    age_strings = [f"these are my friends ages {age} " for age in numbers]
    print(age_strings)



def list_comprehension():
    ages = [43,23,14,54,52,75]\
    ## iterable dedo phele fir iterate krvao and then condition
    odd_ages = [i for i in ages if i % 2 == 1]
    print(odd_ages)



    ## guest and friend of the list
    
    
def dictionary_comprehension():
    friends = ["Rolf", "Bob", "Jen", "Anne"]
    time_seen_since = [1,4,3,5,6,6]

    friends_mapping = {
        friends[i] : time_seen_since[i]
        for i in range(len(friends))
    }

    print(dictionary_comprehension)

"""
    break comes out of the loop
    whreas continue goes to the next iteration of the loop

    mtlb vo us iteration ko skip krke agle iteration pr chla jata h

"""

if  __name__ == "__main__":
    dictionary_comprehension()