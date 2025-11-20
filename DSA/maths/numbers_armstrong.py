# https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
class Solution:
    def armstrongNumber (self, n):
        num = n
        final = 0
        while num:
            a = num % 10
            final += pow(a,3)
            num = num //10
            
        if n == final:
            return True
        else:
            return False

