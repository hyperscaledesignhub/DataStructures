def N_queens(num:int):
    result=[]
    def is_conflict(slate:list[int],col:int):
        for row in range(len(slate)):
            if slate[row] == col:
                return False
            #We want to see the difference of conflict between 
            #the (row,slate[row]) and (len(slate),col)
            #rowdiff = 
            rowdiff = abs(row-len(slate))
            coldiff = abs(col-slate[row])
            if rowdiff == coldiff:
                return False
        return True
    def helper(i:int,slate:list[int]):
        #Base case
        if i == num:
            result.append(slate[:])
            return    
        
        #Recursive case
        for col in range(0,num):
            if is_conflict(slate,col):
                slate.append(col)
                helper(i+1,slate)
                slate.pop()
    helper(0,[])
    return result
r=N_queens(4)
print(f" Result of N queens is {r}")