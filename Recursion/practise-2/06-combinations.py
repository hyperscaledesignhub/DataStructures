def combinations(nums:list[str],comb_size:int):
    result=[]
    def helper(slate:list[str],i:int):
        #Base case
        if i == comb_size:
            result.append(slate[:])
            return
        #Recursive case
        for k in range(i,len(nums)):
            slate.append(nums[k])
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input=['A','B','C','D']
r=combinations(input,2)
print(f"combinations of {input} for size 2 is {r}")