def letter_case_permute(s:str):
    result = []
    
    def helper(slate:str,i:int):
        #Base case
        if i == len(s):
            result.append(slate[:])
            return
        
        #recursive case
        #Check digit, if digit, i add to the slate
        #after that i call subordinate to process
        #the string at position 'i+1', he repeats 
        #same thing
        if s[i].isdigit():
            helper(slate+ s[i],i+1)
            #Here slate state is before as it was, 
            #not changed, hence no need to clean up
            #also need to check what happens when not
            #cleaned later
        else:
            #now i add to slate while calling subordinate
            #the upper case and lower case
            helper(slate+s[i].upper(),i+1)
            helper(slate+s[i].lower(),i+1)
    helper("",0)
    return result
input="a1bcd"
r=letter_case_permute(input)
print(f"letter case permutation of input {input} is {r}")

    
        
        