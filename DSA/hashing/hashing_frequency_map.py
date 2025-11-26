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

n = len(nums)

hash_map=dict()
# T.C in dictionary on a average is O(1) once in  a blue moon that too under collisions it will give O(n)

# .get method returns the value for the specified key if key is in dictionary. 
# else it returns default value 0 or any specified value


for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

print(hash_map)

    