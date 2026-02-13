def permutation(nums:list[int]):
    result=[]
    def helper(nums:list[int],i:int,slate:list[int]):
        #Base case
        if i == len(nums):
            result.append(slate[:])
            return
        
        #Recursive case
        for k in range(i,len(nums)):
            nums[i],nums[k] = nums[k],nums[i]
            #In permutation repetetiveness shouldn't be there
            #Thats the reason what we are doing is
            #We have running index 'k', which is always kept
            #at the i'th position, we are adding i'th value
            #To the slate. And we are calling our subordinates 
            #To process from i+1 onwards
            #This running index we are adding 
            slate.append(nums[i])
            helper(nums,i+1,slate)
            #If i haven't removed from slate, current slate
            #value is being used in all next iterations
            slate.pop()
    helper(nums,0,[])
    return result
li =[1,2,3]
r=permutation(li.copy())
print(f"Permutation of {li} is {r}")