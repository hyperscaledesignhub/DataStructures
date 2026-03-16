#Combinations are nothing but generation of subsets of specified length

#Same as generation of subsets but with the length of the combination size 
# like N(c,r) 
def combination(nums:list[int], size:int):
    result =[]
    def helper(slate:list[int],i:int):
        #Same as inclusive and exclusive 
        #Once slate size equal to combination size then
        #Add that result to the slate and come out 
        #Thats why base case is when i equal to combination
        #This is called selection of items without any repetetion 
        #size then come out 
        if len(slate) == size:
            result.append(slate[:])
            return
        #This case is also mandatory since 
        if i == len(nums):
            return
        
        #Recursive case 
        #exclusive case
        helper(slate,i+1)
        slate.append(nums[i])
        helper(slate,i+1)
        slate.pop()
    helper([],0)
    return result
input=[1,2,3,4]
size=2
r=combination(input,size)
print(f"Combination of {input} and size ={size} is C({len(input),size} is {r}")