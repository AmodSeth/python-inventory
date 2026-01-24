#  lexicographically
# If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0".


# if s1 < s2 = -1
# if s1 > s2 = 1
# if s1 == s2 = 0


def solve():
    s1 = input().strip().lower()
    s2 = input().strip().lower()
    
    
    letter_count_s1 = [ord(c) for c in s1]
    letter_count_s2 = [ord(c) for c in s2]

    sum1 = letter_count_s1
    sum2 = letter_count_s2

    if sum1 < sum2:
        print("-1")
    elif sum1 > sum2:
        print("1")
    else:
        print("0")

         
        
    

    




solve()