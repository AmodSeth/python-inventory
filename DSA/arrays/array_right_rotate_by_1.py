 # Right Rotate Array by 1
nums = [5,-2,3,9,0,6,10,7]

def using_list_slicing():
    # Using list slicing
    n = len(nums)
    #[:] is used to modify the original list in place 
    # else it will create a new list and assign it to nums variable only in local scope
    nums[:] = nums[-1:] + nums[0:n-1]
    return nums


if __name__ == "__main__":
    print(using_list_slicing())

    