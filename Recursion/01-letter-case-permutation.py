def letter_case_permutation(S:str):
    
    result = []
    
    def helper(S:str,i:int,slate:list[str]):
        if i == len(S):
            result.append("".join(slate))
            return
        else:
            if S[i].isdigit():
                slate.append(S[i])
                helper(S,i+1,slate)
                slate.pop()
            else:
                slate.append(S[i].upper())
                helper(S,i+1,slate)
                slate.pop()
                
                slate.append(S[i].lower())
                helper(S,i+1,slate)
                slate.pop()
        return result
    return helper(S,0,[])
st="a1bd"
r= letter_case_permutation(st)
print(f"Value returned is {r}")
