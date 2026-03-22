def generate_parenthesis(count:int):
    result=[]
    def helper(lcount:int,rcount:int,slate:list[int]):
        if rcount < lcount or rcount < 0 or lcount < 0:
            return
        if rcount == lcount == 0 :
            result.append(slate[:])
            return
        slate.append('(') 
        helper(lcount-1,rcount,slate)
        slate.pop()
        slate.append(')')
        helper(lcount,rcount-1,slate)
        slate.pop()
    helper(count,count,[])
    return result
paranthesis_count=2
r=generate_parenthesis(paranthesis_count)
print(f"result of generate parenthesis with count {paranthesis_count} is {r}")
        
        