"""
# ## first condition
# ## need to find that N where its divible by k
# i.e n%k==0
# given k 
# ## second 
# n can only be make of 1 s
# like 1 , 11, 111, 1111, ....
# for eg:
# print111 % 3 == 0
"""


# thoughts: Note:

# if k is even it cannot be divisible by n made of 1s only 

# brute force approach:
# saare hi options select krlo

# def smallest_brute_force():
#     k = int(input())
#     ## base 
#     ## base case check
#     if k % 2 == 0:
#         return -1
#     for i in range(1, k+1):
#         n = int( '1' * i) 
#         if n % k == 0: 
#             return len(str(n))
#     return -1




# print(smallest_brute_force())

#lol failed at input 9016

## bhai full on maaths lagana padega

def final_solution (k: int) ->int:
    if k % 2 == 0:
        return -1
    n = 0
    for i in range(1, k+1):
        n = (n * 10 + 1) % k
        if n % k == 0:
            return i
    return -1

k = int(input())
print(final_solution(k))