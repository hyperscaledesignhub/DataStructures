def permutation_mutable(S:list[int]):
    
    result =[]
    
    def helper(S:list[int],i:int):
        if len(S) == i:
            result.append(S[:])
            return
        
        else:
            for k in range(i,len(S)):
                S[k],S[i] = S[i],S[k]
                helper(S,i+1)
                S[k],S[i] = S[i],S[k]
        return result
    return helper(S,0)
input=[1,2,3]
r=permutation_mutable(input)
print(f"final result of permutation {input} is {r}")

    