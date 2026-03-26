#This problem prints all expressions that leads to given target
#For ex: 16 is the traget expressions are (1+1+.. +1); 32/2; (8 + 16/2)
#like this need to print all expressions 
# for this total we have +, -, *,/  are the 4 types are there
#For each type we need to create and evaluate them based on precedence
#For creation we use recursion
#We have4 symbols-> +, -, *,/ 
def expression_eval(target:int):
    result=[]
    def evaluate_expr(num1:int,num2:int,expr:str):
        r=[0]
        match expr:
            case '+':
                r[0] = num1+num2
            case '-':
                r[0] = num1-num2
            case '*':
                r[0] = num1*num2
            case '/':
                if num2 != 0 and num1 % num2 == 0:  
                    r[0] = num1//num2
                else:
                    return -1
                
        return r[0]
            
    def helper(output:int,num1:int,slate:list[str]):
        if output == target:
            result.append(slate[:])
            return
        if num1 > target or output < 0:
            return
        for op in ['+','-','*','/']:
            if op == '/' and num1 == 0:
                continue
            val=evaluate_expr(output,num1,op)
            if val < 0 or val == 0:          # subtraction went negative, skip                                                  
                continue
            if op in ['+', '*'] and val > target:   # growing too large, skip                                       
                continue    
            st=str(output) + op + str(num1)
            slate.append(st)
            #print(f"slate is {slate}")
            helper(val,num1+1,slate)
            slate.pop()
    helper(1,2,['1'])
    return result
            
r=expression_eval(16)
print(f" Result of expression is {r}")
        
    