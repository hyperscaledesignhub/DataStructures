def combinations(input:list[str],size:int):
    result=[]
    n = len(input)
    def helper(slate:list[str],i:int):
        #base case-1
        if len(slate) == size:
            result.append(slate[:])
            return 
        #base case-2
        #Once on intermediary results having slate size < size and exceeded
        #all levels of i, then we must return otherwise this is going 
        #to create stack overflow
        if n == i:
            return
        #Now recursive case which is inclusive and exclusive 
        
        #Exclusive case
        helper(slate,i+1)
        slate.append(input[i])
        #Inclusive case
        helper(slate,i+1)
        slate.pop()
    helper([],0)
    return result
input=['A','B','C','D']
size=3
r=combinations(input,size)
print(f"Output of the combinations of size {size} is {r}")