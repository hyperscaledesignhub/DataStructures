def letter_case_permute_optimise(st:str):
    result = []
    #This program we are using mutable string which is optimised
    #we don;t create a new string in stack over every call. Rather
    #single list of strings is created and used throughout the program
    def helper(slate:list[str], i:int):
        #Base case
        if i == len(st):
            result.append(slate[:])
            return
        
        #Recursive case
        if st[i].isdigit():
            #Now add the digit to the slate
            slate.append(st[i])
            helper(slate,i+1)
            slate.pop()
        else:
            slate.append(st[i].lower())
            helper(slate,i+1)
            slate.pop()
            
            slate.append(st[i].upper())
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input="a1bc"
r=letter_case_permute_optimise(input)
print(f"Given input = {input} result is {r}")
    