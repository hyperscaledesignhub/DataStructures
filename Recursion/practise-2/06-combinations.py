def combinations(nums:list[str],comb_size:int):
    result=[]
    n=len(nums)
    def helper(slate:list[str],i:int):
        #Base case
        if len(slate) == comb_size:
            result.append(slate[:])
            return
        if i == n:
            return
            
        #Exclude case
        helper(slate,i+1)
        #Include case
        slate.append(nums[i])
        helper(slate,i+1)
        slate.pop()
    helper([],0)
    return result
input=['A','B','C','D']
r=combinations(input,2)
print(f"combinations of {input} for size 2 is {r}")