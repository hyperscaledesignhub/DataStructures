def letter_case(st:str):
    result=[]
    def helper(slate:str,i:int):
        #Base case
        if i == len(st):
            result.append(slate[:])
            return
        #recursive case
        if st[i].isdigit():
            helper(slate+st[i],i+1)
        else:
            helper(slate+(st[i].lower()),i+1)
            helper(slate+(st[i].upper()),i+1)
    helper("",0)
    return result
def subsets(input:list[int]):
    result =[]
    def helper(slate:list[int],i:int):
        #Base case
        if i == len(input):
            result.append(slate[:])
            return
        #recursive case
        #Exclude number 
        helper(slate,i+1)
        #Include number
        slate.append(input[i])
        helper(slate,i+1)
        #Clean number added otherwise results of past 
        #are kept remaining in slate
        slate.pop()
    helper([],0)
    return result
def permutations(input:list[int]):
    result=[]
    def helper(slate:list[int],i:int):
        #Base case
        if i == len(input):
            result.append(slate[:])
            return
        #Recursive case
        for k in range(i,len(input)):
            slate.append(input[k])
            #Added kth element to slate at position i
            #Now its time to move kth element to position i
            #with swapping
            input[k],input[i] = input[i],input[k]
            #call subprdinate which takes care of rest
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
    
            
letter_case_input="a1b2"
r=letter_case(letter_case_input)
print(f"letter case permutations is {r}")
subsets_input=[1,2,3]
r=subsets(subsets_input)
print(f"subsets result is {r}")

permute_inputs=[1,2,3]
r=permutations(permute_inputs)
print(f"permute input  result is {r}")
        