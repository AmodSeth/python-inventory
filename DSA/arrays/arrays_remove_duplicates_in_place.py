nums = [1, 2, 2, 3, 4, 4, 5]

# it means ki saare unique elements ko leke aao and array ke sbse aage rakh do 
# and bache use last places pe kuch bhi rkh do 

def removeDuplicates(nums):
    n = len(nums)
    # base case
    if n == 0:
        return 0
    