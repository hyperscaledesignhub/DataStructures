def subsets(s:list[str]):
    result = []
    
    def helper(slate:list[str],i:int):
        
        #Base case, suppose i am already seeing 
        #index i is equal to length of the slate
        #then add the result
        if i == len(s):
            result.append(slate)
            return
        #Recursive case
        #Exclude s[i], by calling subordinate with next
        #element to fill, this handles all elements from i+1'st
        #position in the slate
        helper(slate,i+1)
        #Now include the element at [i] in the slate
        # and pass to the subordinate
        
        helper(slate+ [s[i]],i+1)
    helper([],0)
    return result
input=["1","2","3"]
r=subsets(input)
print(f"subsets of the set {input} is {r}")

        