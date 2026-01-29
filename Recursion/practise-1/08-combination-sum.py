def combination_sum(sum_values:list[int],target:int):
    
    result = []
    sum_values.sort()
    
    def helper(i:int,target:int,slate:list[int]):
        #Base case-1
        if target < 0:
            return
        if target == 0:
            result.append(slate[:])
            return
        if i == len(sum_values):
            return
        
        
        
        #Recursive case
        
        count = 1
        j = i+1
        #Find out how many duplicates are there for the given
        #sum_values at positon i, count stores total values
        #of aum_value[i] that are present at 'i'
        while j < len(sum_values) and sum_values[j] == sum_values[i]:
            count +=1
            j +=1
        for copies in range(0,count+1):
            num_val = sum_values[i]
            
            #the given number of copies of the element at i
            # is greater then target value, then break
            if target - num_val*copies < 0:
                break
            #Now we can add the current count of copies
            #into the slate. Let's add the current count of
            #copies into the slate with an inner loop
            #These copies are eligible to be added to slate
            #since their sum is less than target
            for cp in range(copies):
                slate.append(num_val)
            
            #Now call the subordinate to find the remaining elements
            #that sum to to target. I have added here my count
            #remaining added by subordinate.
            # this subordinate is going to add to slate
            #with the new elements whose target = target-(num_val)*copies
            
            helper(i+count,target - (num_val*copies), slate)
            
            #my subordinate came back by adding, hence 
            #i am cleaning the slate
            
            for cp in range(copies):
                slate.pop()
    helper(0,target,[])
    return result
input=[10,1,2,7,6,1,5]
target=8
r=combination_sum(input,target)
print(f"combination_sum of input {input} and target{target} are: {r}")

            
                
                
        
        