def letter_case_permutation_optimize(S:str):
    result = []
    
    def helper(S:list[str],i:int):
        
        if i == len(S):
            result.append(''.join(S))
        else:
            if S[i].isdigit():
                helper(S,i+1)
            else:
                S[i] = S[i].upper()
                helper(S,i+1)
                S[i] = S[i].lower()
                helper(S,i+1)
        return result
    return helper(list(S),0)
s="a1bd"
r=letter_case_permutation_optimize(s)
print(f"final result is {r}")
                