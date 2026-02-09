def palindrome_partition(s:str):
    
    result = []
    def is_palindrome(st:str):
        i =0
        while i<= len(st)/2:
            if st[i] != st[len(st)-1-i]:
                return False
            i +=1
        return True
        

    def helper(slate:list[str],i:int):
        
        #Resursive case
        #Always check last position of the slate and return
        #in case it is not a palindrome
        if len(slate) > 0 and not is_palindrome(slate[-1]):
            return
        print("crossed is_palindrome")
        #Now check if position of string is already equal
        #to max length of the string then add the result
        #to the slate and return
        if len(s) == i:
            result.append(slate[:])
            return
        #i am calling i to len(string) number of 
        #suordinates, each subordinate add to slate
        #i to pick value for ex: i =2, there are 2,3,4,5
        #subordinates called
        #2- adds-> [2] string, 3-> adds [2-3] string,
        #4-> add [2-4] string,  
        #if any of them are palindromes they are added to the
        #result and come back 
        #When intialised i call from 0 to 4 subordinates
        #ist subordinate add a and find all palindromes possible
        #with a second subordinate takes aa and addds all possible palindromes
        
        #3rd one adds aab, 4th aaba 5th aabaa like this
        for pick in range(i, len(s)):
            slate.append(s[i:pick+1])
            helper(slate,pick+1)
            slate.pop()
    helper([],0)
    return result
input = 'aabaa'
r=palindrome_partition(input)
print(f"Output of palindrome partition of input = {input} is {r}")
    