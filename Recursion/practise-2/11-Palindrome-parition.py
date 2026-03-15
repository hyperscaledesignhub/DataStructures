def palindrome_part(input:str):
    result=[]
    def is_palindrome(st:str):
        i=0
        while i <= len(st)/2:
            if st[i] != st[len(st)-1-i]:
                return False
            i +=1
        return True
    #We have input params slate and the index 
    #position of the string 'i' 
    def helper(slate:list[str],i:int):
        if len(slate) >0  and not is_palindrome(slate[-1]):
            return
        if i == len(input):
            result.append(slate[:])
            return
        for k in range(i,len(input)):
            slate.append(input[i:k+1])
            helper(slate,k+1)
            slate.pop()
    helper([],0)
    return result
input="aabaa"
r=palindrome_part(input)
print(f"Palindrome partition of {input} is {r}")

        