#Arranging the items without repetetion over a line 
def permutation(input:list[int]):
    result = []
    
    def helper(slate:list[int],i:int):
        #Base case
        if i == len(input):
            result.append(slate[:])
            return
        #recursive case
        
        #i am going to add at pos i, every time
        #kth element such that i always provides 
        #to my subordinates different element to start
        #with and my subordinates are going to fill the
        #slate all permutations that starts with kth number
        for k in range(i,len(input)):
            input[k],input[i] = input[i],input[k]
            slate.append(input[i])
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input=[1,2,3]
r=permutation(input)
print(f"Permutation of input{input} is {r}")
    