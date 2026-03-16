def permute_unique(S:list[int]):
    result =[]
    
    def helper(S:list[int],i):
        if i == len(S):
            #print(f"result is {result}")
            result.append(S[:])
            return
        else:
            hmap={}
            for k in range(i,len(S)):
                if S[k] not in hmap:
                    hmap[S[k]] = 1
                    S[k],S[i] = S[i],S[k]
                    helper(S,i+1)
                    S[k],S[i] = S[i],S[k]
        return result
    return helper(S,0)
input=[3,3,0,3]
r=permute_unique(input)
print(f"result of permutation of {input} is {r}")
                
                    
                
                