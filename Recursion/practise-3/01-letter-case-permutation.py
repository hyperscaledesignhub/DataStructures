#This is letter case permutation problem
#Here we are using fixed number of helpers
#Based on the following:
#Every position in the slate helper is going to 
#add capital or small letter 
#And This is constant across each position in the slate 
#Hence number of helpers are fixed they don't depend 
#on the position
def letter_case(input:list[str]):
    result=[]
    def helper(i:int,slate:list[str]):
        #Base case
        if i == len(input):
            result.append(slate[:])
            return
        #Recursive case
        if input[i].isdigit():
            slate.append(input[i])
            helper(i+1,slate)
            slate.pop()
        else:
            slate.append(input[i].lower())
            helper(i+1,slate)
            slate.pop()
            slate.append(input[i].upper())
            helper(i+1,slate)
            slate.pop()
    helper(0,[])
    return result
input=['a','1','b','c']
r=letter_case(input)
print(f"The result of letter case is {r}")
