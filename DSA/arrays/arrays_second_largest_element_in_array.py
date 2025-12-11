# Second largest element in an array

nums = [55, 32, -97, 99, 3,67, 99]

def first_attempt():
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
    return second_largest


def best_solution():
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        ## remember to check that it is not equal to largest :: duplicate max element case
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]

if __name__ == "__main__":
    print(first_attempt())

