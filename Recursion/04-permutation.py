def permutation(nums:list[int]):
    result =[]
    def helper(nums:list[int],i:int,slate:list[int]):
        
        if i == len(nums):
            result.append(slate[:])
            return
        for k in range(i,len(nums)):
            nums[i],nums[k] = nums[k],nums[i]
            slate.append(nums[i])
            helper(nums,i+1,slate)
            slate.pop()
            nums[i],nums[k] = nums[k],nums[i]
        return result
    return helper(nums,0,[])
li = [1,2,3,4]
r=permutation(li)
print(f"permutation of {li} is {r}")
    
            