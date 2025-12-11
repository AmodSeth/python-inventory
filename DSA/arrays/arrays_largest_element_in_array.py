# Find the largest element in an array

# things to ask the interviewer, Does the array only contian the positive numebrs?

nums = [55, 32, -97, 99, 3,67]

def first_attempt():
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            largest = nums[i]
    return largest
            


def case_where_0_would_fail():
    negative_nums= [-1,-2,-3,-4]
    largest = 0
    for i in range(len(negative_nums)):
        if negative_nums[i] > largest:
            largest = negative_nums[i]

    return largest

# T.C = O(n)
def method_1():
    largest = nums[0]
    print(nums)
    n = len(nums)
    for i in range(0,n):
        largest = max(largest, nums[i]) # same as if else condition
    return largest ## saale return to lga

def method_2():
    largest = float("-inf")
    print(nums)
    n = len(nums)
    for i in range(0,n):
        largest = max(largest, nums[i]) # same as if else condition
    return largest ## saale return to lga

    

if __name__ == "__main__":
    print(method_2())
