def permutation(input:list[int]):
    result=[]
    def helper(i:int,slate:list[int]):
        #Base case
        if i == len(input):
            result.append(slate[:])
            return
        #Recursive case
        #The reason for using i as the 
        #starting point is, we need helpers
        # at each position equal to the 
        #number available slate positions
        #Given a number [1,2,3]
        # i=0, slate positions availabe are 3
        # i=1.,slate positions available are 2
        # i=2, slate posotions available are 1
        # we need 3 subordinates at i =0,
        # We need 2 subordinates at i=1,
        # We need 1 subordinate at i=0
        # Because i=0 we have 3 options to fill
        # i=1 we have 2 options to fill
        # i=2 we have 1 option to fill 
        
        for k in range(i,len(input)):
            #For the subordinate we 
            #are passing position=1
            #so that subordinate operates from the 
            #position=1, in position 1 we shouldn't 
            #encounter the value we filled at position 0
            #to achieve it, we always swap the 
            #value we added at slot-0 with the actual 
            #value that is present in input, 
            #so that input that we supply to the subordinate
            #Always don;t have the value we filled at slot-0
            #k is the index that shows the value we filled 
            #in slot-0. Hence this index value we always 
            #keep in position-0 of the input. Such that 
            #It never comes to position=1 we are supplying 
            #to the subordinate. 
            #Hence we have to swap pos=k and pos=0 value 
            #always. In generic terms pos=0 value designates 
            #pos=i 
            #add pos=i, input value designated with k
            slate.append(input[k])
            #Now swap 
            input[i],input[k] = input[k],input[i]
            helper(i+1,slate)
            #Revert swap and append
            input[i],input[k]= input[k],input[i]
            slate.pop()
    helper(0,[])
    return result
input=[1,2,3]
r=permutation(input)
print(f"Permutation of input {input} is {r}")