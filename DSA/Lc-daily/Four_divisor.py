nums = [21,4,7]

# check the count of integers divisor
# if count == 4 return the sum of that array








def divisor_count(element):
    res=[]
    for i in range(1,element+1):
        if element % i == 0:
            res.append(i)
    
        
    return res,len(res)
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    sum = 0
    for i in nums:
        res, x = divisor_count(i)
        print(res,x)
        if x == 4:
            for y in res:
                sum +=y
    print(sum)





    def sumFourDivisors(self, nums: List[int]) -> int:

        def divisor_count(element):
            res=[]
            for i in range(1,int(element**0.5)+1):
                if element % i == 0:
                    res.append(i)
                    if i != element // i:
                        res.append(element // i)

            return res,len(res)
            
        sum = 0

        for i in nums:
            res, x = divisor_count(i)
            if x == 4:
                for y in res:
                    sum +=y
        return sum
    

    



