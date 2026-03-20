def combination_sum(input:list[int],sum:int):
    result=[]
    #In combination sum, numbers are repeated and we 
    #need to find the combination sum of the numbers
    #Here idea is repeated number is added for the time
    #it is repeated for. For ex, if a number is repeated 
    #3 times, first time its added to slate, and then 
    #next pos to add slate is next unique number position
    #that means next position is skipped by the count value 
    #equal to number of times this number is repeated
    #After adding to slate the repeated number for equal to
    # number of times its repeated provided the repeated number
    #sum every time repetition is added,is lesser than the target
    #after that call the subordinate,for next position equal to next number 
    #after the repeated number. 
    input.sort()
    
    def helper(slate:list[int],i:int,target:int):
        #Base case
        if target == 0:
            result.append(slate[:])
            return
        if target < 0:
            return
        if i == len(input):
            return
        
        #Recursive case 
        #Find the number of times a number is repeated
        #Take the count of it 
        #Loop through the count and for each count value add that repeated 
        #number for the count times to slate only if the count*num value 
        #is lesser than the target
        count=1
        j=i+1
        while j < len(input) and input[j] == input[j-1]:
            count +=1
            #print(f"Inside the while loop")
            j+=1
        for cp in range(0,count+1):
            if target - (cp*input[i]) < 0:
                break
            new_target=target - cp*input[i]
            for _ in range(cp):
                #print("appended to slate")
                slate.append(input[i])
            #When cp is '0' it is exclusive case of target
            helper(slate,i+count,new_target)
            for _ in range(cp):
                slate.pop()
    helper([],0,sum)
    return result
input=[2,1,3,1,4,1,5,1]
sum=6
r=combination_sum(input,sum)
print(f"combination sum of {sum} for the input {input} is {r}")
            
            
            