def permutation_with_repetetion(st:str):
    result = []
    
    def helper(slate:list[str],i:int):
        print(f"value if i is {i}")
        #Base case
        if i == len(st):
            result.append(slate[:])
            return
        #recursion
        for k in range(0,len(st)):
            slate.append(st[k])
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input = 'ab'
r=permutation_with_repetetion(input)
print(f"Result of the program permutation with repetetion is {r}")
        