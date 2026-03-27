def combinations(n:int,k:int):
    result = []
    
    def helper(i:int,slate:list[int]):
        if len(slate) == k:
            result.append(slate[:])
            return
        if i == n+1:
            return
        #Exclude the current number S[i]
        helper(i+1,slate)
        #Include the current number S[i]
        slate.append(i)
        helper(i+1,slate)
        slate.pop()
    helper(1,[])
    return result
li=[1,2,3,4]
r=combinations(4,2)
print(f"Combination of {li} is {r}")

r=combinations(5,3)
print(f"Combination of {li} is {r}")