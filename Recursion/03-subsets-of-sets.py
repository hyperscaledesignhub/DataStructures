def subsets_of_set(nums:list[int]):
    result = []
    
    def helper(nums:list[int],i:int,slate:list[int]):
        if i == len(nums):
            result.append(slate[:])
        else:
            #Exclude ith number and Include ith number
            helper(nums,i+1,slate)
            slate.append(nums[i])
            helper(nums,i+1,slate)
            slate.pop()
        return result
    return helper(nums,0,[])
input=[2,3,5,6]
r= subsets_of_set(input)
print(f"For the input{input} subsets are {r}")
    
            
        
            