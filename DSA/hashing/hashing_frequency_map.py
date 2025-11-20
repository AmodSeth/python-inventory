# Method 1
# T.C O(N) where n is len of N
nums = [5,6,7,7,1,9,111,1,1,5,1,1]

f_map=dict()

for i in range(0,len(nums)):
    if nums[i] in f_map:
        f_map[nums[i]]+=1
    else:
        f_map[nums[i]]=1

print(f_map)


# Method 2