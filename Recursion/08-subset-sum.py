def subset_sum(S:list[int],target:int):
    
    result =[]
    
    def helper(slate:list[int],slate_sum:int,i:int):
        
        if slate_sum == target:
            result.append(slate[:])
            return 1
        if slate_sum > target:
            return 0
        if i == len(S):
            return 0
        #Now include and exclude rule and generate sum
        helper(slate,slate_sum,i+1)
        slate.append(S[i])
        helper(slate,slate_sum+S[i],i+1)
        slate.pop()
    helper([],0,0)
    return result
input=[1,2,3,4,5]
r=subset_sum(input,5)
print(f"input = {input}, target = 5, output ={r}")

        
    
    