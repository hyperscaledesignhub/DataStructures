def subset_sum(s:list[int],target:int):
    
    result =[]
    
    def helper(slate:list[int],slate_sum:int,i:int):
        #Base case
        
        #1. if the salte_sum equal to target then add the 
        # result and return
        if slate_sum == target:
            result.append(slate[:])
            return
        #2. if i equal to length of s then return
        
        if i == len(s):
            return
        
        #3.  if slate_sum greater than target then return
        
        if slate_sum > target:
            return
        
        #recursive case
        #Exclude the given index element and call subordinate
        #Each of them add to slate subsets whose sum is equal to the
        #target and return back here
        
        helper(slate,slate_sum,i+1)
        
        #Include the given index element and call subordinate
        
        slate.append(s[i])
        helper(slate,slate_sum+s[i],i+1)
        slate.pop()
    helper([],0,0)
    return result
s=[1,2,3,4,5]
target=5
r=subset_sum(s,target)
print(f"For the given subset {s} and target {target} following is the result = {r}")