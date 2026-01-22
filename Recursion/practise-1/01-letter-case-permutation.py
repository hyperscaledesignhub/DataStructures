def letter_case_permute(s:str):
    result = []
    def helper(slate:str,i:int):
        
        #See i am an intermediate manager at some position
        #Hence first i check whether i am the last manager
        #By checking the length of the slate indicated by i
        #has reached already to the end. And then i just append
        # the result in case already all elements are covered
        # And then return the result
        
        if len(s) == i:
            result.append(slate)
            return
        
        
        #Recursive case, call subordinates who will do
        #their job of adding i+1'st element to the slate
        #i will be adding i'th element to the slate
        #and returning back
        if s[i].isdigit():
            #Now call a single subordinate just to add digit to
            #the slate
            helper(slate+s[i],i+1)
        else:
            #Now here call 2 subordinates, one is sending lower case letter
            #Other is sending upper case letter
            #I am adding to slate lower case letter and 
            #while calling the subordinate
            helper(slate+s[i].lower(),i+1)
            #Here i am calling subordinate, which call using upper case letter
            helper(slate + s[i].upper(),i+1)
    helper("",0)
    return result
input="a1bd2"
r=letter_case_permute(input)
print(f"letter case permute of: {input} is {r}")

            
