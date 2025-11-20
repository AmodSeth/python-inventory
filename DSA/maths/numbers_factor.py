#https://www.geeksforgeeks.org/problems/all-divisors-of-a-number/1 

## Brute Force Method --> but gave TLE
## T.C O(N)  
# S.C O(k) k would be the total number of factors
class Solution:
    def print_divisors(self, N):
        # code here
        for i in range(1, N+1):
            if N % i == 0:
                print(i,end=" ")


# ## Better Approch T.C O(N)
# using i*i <= N

"""
## Optimized Approach 
# T.C O(sqrt(N))
 if N  == 36 
 then factors are
 1 -- 36
 2 -- 18
 3 -- 12
 4 -- 9
 6 -- 6
we go from num to sqrt (N) but this doesn't give them in order
"""


def factors(num: int) -> List[int]:
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            if num // i != i:
                factors.append(num // i)
    factors.sort()  # Do this only if you want in sorted order
    return factors


