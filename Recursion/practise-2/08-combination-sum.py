def subset_sum_duplicates(nums:list[int],sum:int):
    result=[]
    nums.sort()
    def helper(slate:list[int],target:int,i:int):
        if target < 0:
            return
        #Base case, same as regular subset sum 
        if target == 0:
            result.append(slate[:])
            return 
        if i == len(nums):
            return
        count=1
        j=i+1
        #count duplicates
        while j < len(nums) and nums[j] == nums[j-1]:
            count +=1
            j +=1
        #now go through each count value by adding to slate
        for copies in range(0,count+1):
            
            #check if copies value greater than target, if its
            #then break this loop 
            if target - (copies*nums[i]) < 0:
                break 
            #adding copies won't be lesser than the target, hence 
            # we can add these many numbers to the slate
            for cp in range(copies):
                slate.append(nums[i])
            #now call the subordinate to find the remaining
            #combinations after adding copies of values to slate
            new_target=target - (copies*nums[i])
            helper(slate,new_target,i+count)
            #Now clean slate such that it shouldn't have old values 
            for cp in range(copies):
                slate.pop()
    helper([],sum,0)
    return result
input=[1,1,1,1,4,2,5]
sum=6
r=subset_sum_duplicates(input,sum)
print(f"For the given input = {input} and combination values of sum = {sum} are {r}")

            