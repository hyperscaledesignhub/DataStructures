def lettercase_permute(s:list[str]):
    #Here we don't use stack to create a new str value
    #Each time, instead we use a single variable always
    #And call the same copy. Here strategy is whenever 
    #i call before calling i add variable to the reference
    #Data that i had after finishing the function call i am
    #deleting it.
    result = []
    def helper(slate:list[str],i:int):
        #Same as before, last i am adding the termination
        #condition in case i am the last manager
        if i == len(s):
            #Here if we append slate as is, it 
            # is going to add the final state which is
            #decided by the final manager, hence we need to
            # add the current state as a clone
            result.append(slate[:])
            return
        #Now same as before, but follow the rule here, single state
        #across all
        if s[i].isdigit():
            slate.append(s[i])
            helper(slate,i+1)
            #Clean the element added by me, after 
            #my subordinates comes back by adding their results
            #to the slate
            slate.pop()
        else:
            slate.append(s[i].lower())
            helper(slate,i+1)
            slate.pop()
            slate.append(s[i].upper())
            helper(slate,i+1)
            slate.pop()
    helper([],0)
    return result
input=['a','1','b','d','2']
r=lettercase_permute(input)
print(f"Given input ={input}, letter case permute is {r}")
