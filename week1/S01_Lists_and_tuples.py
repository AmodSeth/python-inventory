def list_practise():
    # to create a list we use square brackets[]
    my_list = [1, 2, 3, 4,]
    print(len(my_list))  # prints the length of the list
    # to append into the list
    my_list.append(5)
    print(len(my_list))

    friends = [["John", 25], ["Jane", 30], ["Doe", 22]]
    ## to add into the list
    friends.append(["Smith", 28])

    ## to remove from the list
    """
    we need to give the whole list name element to remove it
    """
    friends.remove(["Doe", 22])



def tuple_practise():
     #brackets are not required to create a tuple
    my_tuple = (1, 2, 3, 4)
    tuple_2 = 1,2,3,4
    print(type(my_tuple))

    var_1 = "hello" # string
    var_2 = "hello", # tuple with one element it only needs a comma

    # we can't add into a tuple
    # we can't remove from a tuple

   


def sets_practise(): 
    # sets are created using curly braces {}

    science_subjects = {"Physics" , "Chemistry", "Biology"}

    science_subjects.add("Maths") # to add into a set

    science_subjects.remove("Biology") # to remove from a set

    science_subjects.add("Maths")

    print(science_subjects) 

def advanced_sets_practise():
    art_group = {"History", "Geography", "English"} #Set 1
    science_subjects = {"Physics" , "Chemistry", "Biology"} #Set 2

    art_but_not_in_science = art_group.difference(science_subjects)

    science_but_not_in_art = science_subjects.difference(art_group) 

    art_and_science = art_group.intersection(science_subjects) 



def dictionary_practise():
    ## tuples of dictionary
    friend_ages = (
       { "Amod" : 25 }  ,
       { "John" : 30 } , 
       { "Jane" : 22 }, 
    )

    print(friend_ages[0]["Amod"]) # to access the value of a key


"""
if __name__ == "__main__": means
“Run this part only when file is executed directly, not when imported.”

"""

if __name__ == "__main__": 
    dictionary_practise()



