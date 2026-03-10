def generate_parenthesis(count:int):
    result = []
    def helper(left_count:int,right_count:int,slate:list[str]):
        if left_count > right_count or left_count < 0 or right_count < 0:
            return
        
        
        if left_count == right_count == 0:
            result.append(slate[:])
            return
        slate.append("(")
        helper(left_count-1,right_count,slate)
        slate.pop()
        slate.append(")")
        helper(left_count,right_count-1,slate)
        slate.pop()
    helper(count,count,[])
    return result
size=2
r=generate_parenthesis(size)
print(f"for size= {size} parenthesis are {r}")
        
        