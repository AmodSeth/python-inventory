nums = [1,1,1,1,2,2,2,2,2,3,3,4,5,5,6,9,8,1]


def remove_duplicates_in_place(nums):
    map_1 = dict()
    ## get the map of range
    for i in range(len(nums)):
        if nums[i] in map_1:
            map_1[nums[i]] += 1
        else:
            map_1[nums[i]] = 1

    
    keys = list(map_1.keys())

    for i in range(len(keys)):
        nums[i] = keys[i]

    return nums


    



    
    



if __name__ == "__main__":
    print(remove_duplicates_in_place(nums))