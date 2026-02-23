def subset_sum(nums:list[int],sum:int):
    result=[]
    input_size=len(nums)
    def helper(slate:list[int],i:int,target:int):
        #Base case
        if target == 0:
            result.append(slate[:])
            return
        if i == input_size:
            return 
        #Generate subsets with include and exclude 
        helper(slate,i+1,target)
        slate.append(nums[i])
        new_target = target - nums[i]
        helper(slate,i+1,new_target)
        slate.pop()
    helper([],0,sum)
    return result
input=[1,2,3,4,5]
sum = 6
r=subset_sum(input,sum)
print(f" For the given input {input} and target sum {sum}, results are {r}")