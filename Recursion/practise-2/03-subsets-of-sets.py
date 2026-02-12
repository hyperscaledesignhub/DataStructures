#subsets are based on include and exclude principle 
#Suppose we take 2 numbers how many subsets are formed?
# [1,2] => include 1, [1], exclude 1 -> [], for these two again for [1] include 2
#[1,2], [2], exclude 2, [1] and []
def subsets_of_sets(nums:list[int]):
    result = []
    
    def helper(slate:list[int], i:int):
        #Base case
        if i == len(nums):
            result.append(slate[:])
            return
        #Resursive case 
        #call 2 subordinates one excludes i'th element
        #Other includes i'th element
        #Exclude case
        helper(slate,i+1)
        #include case
        slate.append(nums[i])
        helper(slate,i+1)
        slate.pop()
    helper([],0)
    return result
input = [1,2,3]
r=subsets_of_sets(input)
print(f"The result of subsets of sets for input = {input} is {r}")