#This is the permutation with duplicate numbers 
def permutation_with_duplicates(nums:list[int]):
    result = []
    
    def helper(slate:list[int],i:int):
        #Base case
        if i == len(nums):
            result.append(slate[:])
            return
        #Recursive case
        #Here we are adding to the slate from
        #position i to len(num) by any subordinate
        #That means 0th subordinate adding in first slot
        #3 numbers, 1st subordinate from 1'st slot from
        #2 to 3. 2nd subordinate at slot 3
        hmap={}
        for k in range(i,len(nums)):
            #Check that duplicate number before adding to slate
            #Because same number repeats create same set of permutations
            if nums[k] not in hmap:
                #At slot i always add unique number, that number must
                #not be shared with the subordinate.
                hmap[nums[k]] = 1
                nums[k],nums[i] = nums[i],nums[k]
                slate.append(nums[i])
                helper(slate,i+1)
                nums[k],nums[i] = nums[i],nums[k]
                slate.pop()
    helper([],0)
    return result
input=[1,2,2,3]
r=permutation_with_duplicates(input)
print(f"Permutation with duplicates with input: {input} is {r} ")
    