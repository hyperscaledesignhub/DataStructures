def subset_sum(input:list[int],sum:int):
    result=[]
    def helper(i:int,slate:list[int],target:int):
        #Base case 
        if target == 0:
            result.append(slate[:])
            return
        
        if i == len(input):
            return
        #Recursive case
        
        #Exclusive case 
        helper(i+1,slate,target)
        
        #Inclusive case
        slate.append(input[i])
        helper(i+1,slate,target-input[i])
        slate.pop()
    helper(0,[],sum)
    return result
input=[1,4,2,3,7]
sum=6
r=subset_sum(input,sum)
print(f"Given {input} and target sum {sum}, result is {r} ")