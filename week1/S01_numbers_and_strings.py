def numbers_practice():
    age = 30

    PI = 3.14

    # pemdas - parenthesis, exponents, multiplication, division, addition, subtraction is followed
    maths_operations = 1 + 2 * 3 / 4 - 5 #after devision it will always give a float value even if the result is a whole number
    print(maths_operations)


    # float division
    float_division = 3 / 2
    print(float_division)

    # integer division
    int_division = 3 // 2
    print(int_division)



def string_practise():
    string_with_quotes = "Hello, I'm a string with quotes"
    string_with_double_quotes = 'Hello, I\'m a string with double quotes' # escaping the single quote

    multipline_quote = """
    my name is amod seth
    next is string formatting
    """
    

    # limitation of f string
    name = "Amod"
    greeting = f"Hello, my name is {name}"
    print(greeting)
    name = "Seth"
    print(greeting) # it will still print amod because the value of greeting is already set 

    # format method


def boolean_practise():
    my_number = 5
    user_number = int(input("Enter a number: "))

    print(my_number == user_number, end=" ")

    ## and or enviornment
    x = True
    cmp = x and 18
    print(cmp)
    ## case 2
    age = int(input("Enter your age: "))
    side_job = True
    print(age > 18 and age < 65 or side_job)


    return 




### starter function
def main():
    boolean_practise()


if __name__ == "__main__":
    main()