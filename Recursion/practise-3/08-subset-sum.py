def subset_sum_duplicates(input:list[int],target:int):
    result=[]
    input.sort()
    def helper(slate:list[int],i:int,sum:int):
        
        if sum < 0:
            return
        #base case
        if sum == 0:
            result.append(slate[:])
            return
        if i == len(input):
            return
        
        #First we need to count the duplicates 
        #Suppose there are 3 duplicates, add to slate 
        #1 duplicate, 2 duplicates, 3 duplicates 
        #and then add the rest of the numbers to the slate
        #one after the other
        #Recursive definition
        j=i+1
        count=1
        while j!=len(input) and input[j-1] == input[j]:
            count +=1
            j +=1
        for dupes in range(0,count+1):
            #First check dupes*input[i] is greater than
            #target, if its, break from this loop
            #If not, then proceed
            if target - dupes*input[i] < 0:
                break
            for cp in range(dupes):
                slate.append(input[i])
            new_sum=sum - dupes*input[i]
            helper(slate,i+count,new_sum)
            for cp in range(dupes):
                slate.pop()
    helper([],0,target)
    return result
input=[1,2,1,3,1,4,1,5]
sum=6
r=subset_sum_duplicates(input,sum)
print(f"result of subset sum of{sum} is {r} ")


                
    