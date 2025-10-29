"""
using the maths way
"""

from math import *
def count_numbers ():
    n = int(input(""))
    log_value = int(log(n,10)  + 1)
    print(log_value)


"""
using the normal way
always use the float division
T.C = O(log base 10)

## mtlb jisse bhi divide horha hain to 
vo usi se hi log ho rha hain


"""

def count_numbers_normal():
    n = int(input(""))
    count = 0
    while n > 0:
        n = n // 10
        count +=1
    print(count)








if __name__ == "__main__":
    count_numbers_normal()
