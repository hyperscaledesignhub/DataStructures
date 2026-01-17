def combination_sum(sum_values:list[int], target:int):
    
    result = []
    sum_values.sort()
    
    def helper(i:int,target:int,slate:list[int]):
        
        if target < 0:
            return
        if target == 0:
            result.append(slate[:])
            return
        if i == len(sum_values):
            return
        count = 1
        j = i+1
        while j < len(sum_values) and sum_values[j] == sum_values[i]:
            count +=1
            j +=1
        for copies in range(0,count+1):
            num_val = sum_values[i]
            
            if target - num_val*copies < 0:
                break
            for op in range(copies):
                slate.append(num_val)
            helper(i+count,target-(num_val*copies),slate)
            for op in range(copies):
                slate.pop()
    helper(0,target,[])
    return result
input=[10,1,2,7,6,1,5]
target=8
r=combination_sum(input,target)
print(f"combination_sum of input {input} and target{target} are: {r}")
                