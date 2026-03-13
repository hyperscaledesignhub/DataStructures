def subsets(num:list[int]):
    result=[]
    def helper(i:int,slate:list[int]):
        #Base case 
        if i == len(num):
            result.append(slate[:])
            return
        #Recursive case
        #Every position the number of subordinates 
        #Are always fixed hence same template 
        #of subordinates are sufficient 
        helper(i+1,slate)
        slate.append(num[i])
        helper(i+1,slate)
        slate.pop()
    helper(0,[])
    return result
input=[1,2,3]
r=subsets(input)
print(f"Number of subsets of {input} set, are {r}")
        