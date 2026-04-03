def palindrome_partition(input:str):
    #In this program we are going to parttition the string with
    #repect to the palindromes
    #This is how we do: 
    #I am going to start from 0 and keep verifying the palindromes
    #of lengths 1,2,3 ... etc.. i am going to call the subordinate 
    # by passing it palindrome of length 2 between 0-2, 
    #if the subordinate didn't find it as palindrome then it returns 
    #and i am going to pass lenght 3 string between 0:3, if this is 
    #palindrome then my subordinate is going to find the palindrome 
    #partitions starting from 4 to 6. Suppose there are no palindromes
    #between 4 to 6, it returns, after returning, previous palindrome 
    #is removed from the slate.
    #suppose if its able to find palindrome between 4 to 6 
    #Then the result is added to the slate. 
    #And it returns, after that i am going to find palindrome betwen 0 o 3, 
    #If its palindrome then my subordinate is going to partition 
    #between 3 to 6, if its able to then, this continue 
    #Even my subordinate also does the following:
    #from 3 to 4, it tries, no plainfrome, then tries between 3 to 5
    # if there is palindrome, then add to slate, 
    #then its subordinate tries from 5 to 6, if it is palindrome then 
    #it adds to the slate and its subordinate tries from 6 to 6 
    #its palindrome and since i = len(input) here slate 
    #value added to the result and returns 
    #Now the slate added 5 to 6 is removed 
    #The my subordinate is going to remove 3 to 4. 
    #now my subordinate adds 3to 5, string to slate
    #since this if its palindrome then, subordinate 
    # is going to try 5 to 6, if its then its subordintae
    #is going to do 6 to 6,, which is palindrome and
    #this slate also added to result 
    #5 to 6 removed from slate 
    #my subordinate is going to remove the 3 to 5 from slate
    #It tries between 3 to 6.  
    #if its not palindrome then it returns and remove from slate 
    #it comes back to me, i am going to add 1 to 4, string 
    #if its a palindrome then my subordinate is going to try 
    #between 5 to 6 if its added, it calls subordinate 
    #to start from 6, if string between 5 to 6 is palindrome 
    #its added to the result. And it returns 
    def is_palindrome(st:str):
        p = 0
        q = len(st)-1
        while p < q:
            if st[p] != st[q]:
                return False
            p +=1
            q -=1
        return True
    
    result =[]
    def helper(slate:list[str],i:int):
        #Base case 
        #If the string is not palindrome then we can return 
        if len(slate) > 0 and not is_palindrome(slate[-1]):
            return
        #If current index of string scanned equal to last position 
        #then we finished entire string and we can add it to the 
        #result
        if i == len(input):
            result.append(slate[:])
            return
        
        #Recursive case 
        for k in range(i,len(input)):
            slate.append(input[i:k+1])
            helper(slate,k+1)
            slate.pop()
    helper([],0)
    return result
input="aabaa"
r=palindrome_partition(input)
print(f"Result of palindrome partition of input {input} is {r}")
            
            