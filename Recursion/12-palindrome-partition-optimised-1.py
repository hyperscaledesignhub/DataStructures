def palindrome_partition(s:str):
    # Precompute all palindromes using Dynamic Programming
    n = len(s)
    if n ==0:
        return [[]]
    #Precompute Palindrome Table
    # is_palindrome[i][j] = True, if s[i:j+1] is a palindrome
    is_palindrome = [[False]*n for _ in range(n)]
    
    #Every single character is a palindrome
    for i in range(n):
        is_palindrome[i][i] = True
    #Check palindrome of length 2
    for i in range(n-1):
        is_palindrome[i][i+1] = (s[i] == s[i+1])
    #Check palindrome of length or more
    for length in range(3,n+1):
        for i in range(n-length+1):
            j = i+length -1
            is_palindrome[i][j] = (s[i] == s[j]) and is_palindrome[i+1][j-1]
    result = []
    def backtrack(start:int,current_partition:list):
        #Base case, reached end of the string
        if start == n:
            result.append(current_partition[:])
            return
        #Try all possible substrings starting from 'start'
        for end in range(start,n):
            if is_palindrome[start][end]:
                current_partition.append(s[start:end+1])
                backtrack(end+1,current_partition)
                current_partition.pop()
    backtrack(0,[])
    return result
input='aaab'
r=palindrome_partition(input)
print(f"input {input}, palindrome partition = {r}")
        