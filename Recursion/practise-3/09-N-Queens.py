def N_Queens(n:int):
    result =[]
    def is_col_allowed(col:int,slate:list[int]):
        #This is going to assume that the current position is at
        #(len(row),col) for this position, check across all rows 
        #upto < len(row) over a given column 'col' for row=0, 
        #Its (0,col) and (len(row),col) check values slate[0] and 
        # and slate[len(row)] values are same or not if same then
        #there is a conflict
        #similarly, check if rowdiff and coldiff is same for the 
        #diagonal check. But we are checking a single coloumn and
        #multiple rows, then why diagonal check is required?
        #The reason is a foe given row, col is checke by slate[row]
        #this is where queen is placed. So we need to make diagona check
        #like this for ex: (1,1) , (2,2) rowdiff and coldiff both 
        # are same.
        #1'st check is the both columns are same at a given row 
        for row in range(len(slate)):
            #1st check is both cols are same 
            if slate[row] == col:
                return False
            #next check diagonal check 
            #row,col over the running row, is (row,slate[row])
            #similarly (row,col) where we want to place queen is 
            #(len(slate),col) 
            rowdiff = abs(len(slate)-row)
            coldiff = abs(col-slate[row])
            if rowdiff == coldiff:
                return False 
        return True
    def helper(slate:list[int],i:int):
        if i == n:
            #We got the result here that means all cols are successfuly
            #finsihed. Now append the result here
            result.append(slate[:])
            return
        #Recursive case
        #The position of slate shows the row value
        #First i am going to check for all columns 
        #from 0 to n-1 over a row=0. 
        #I am going to find a slot over 0 to n-1 columns 
        #Then i call my subordinate to find col=1 onwards 
        #to find a position
        #First i place col=0 and row=0 then call subordinate 
        #to place col=1,row=1, if subordinate comes back 
        #then i am going to remove whatever i kept before 
        #and try to find col=1 and row=0, and then call 
        #subordinate to find in row=1 into all coloumns 
        #In this process all subordinates will be called 
        #and they get all results and added to the result list already
        for col in range(0,n):
            if is_col_allowed(col,slate):
                slate.append(col)
                helper(slate,i+1)
                slate.pop()
    helper([],0)
    return result
board_size=4
r=N_Queens(board_size)
print(f"Result of board_size = {board_size} is {r} ")
        