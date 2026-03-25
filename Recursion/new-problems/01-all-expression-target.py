#This problem prints all expressions that leads to given target
#For ex: 16 is the traget expressions are (1+1+.. +1); 32/2; (8 + 16/2)
#like this need to print all expressions 
# for this total we have +, -, *,/  are the 4 types are there
#For each type we need to create and evaluate them based on precedence
#For creation we use recursion
#We have4 symbols-> +, -, *,/ 
#First 2 numbers num1,num2 -> give to symbol-1 -> output of it, out-1 we give to 
#symbol-2 along with a new number num3, output of both out-2 and num4 
#we give to symbol-3, output of both out-3 and num5 we give to symbol-4
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
                if num2 !=0: 
                    r[0] = num1//num2
        return r[0]
            
    def helper(num1:int,num2:int,expr:str,slate:list[str],target_value:int):
        value= evaluate_expr(num1,num2,expr)
        print(f"value is {value}")
        if value > target_value or value < 0:
            return
        if num1 > target_value or num2 > target_value:
            return
        if expr!='z':
            slate.append( " + ("+ str(num1) + ")" + expr + "("+ str(num2) + ")" )
        #print(f"slate is {slate}")
        if value == target_value:
            result.append(slate[:])
            #print(f"result is {result} ")
            return
        new_target=target_value-value
        helper(num1+1,num2+1,'+',slate,new_target)
        helper(num1+1,num2+1,"-",slate,new_target)
        helper(num1+1,num2+1,'/',slate,new_target)
        helper(num1+1,num2+1,"*",slate,new_target)
        if expr !='z':
            slate.pop()
    helper(0,0,"z",[],target)
    return result
r=expression_eval(16)
print(f" Result of expression is {r}")
        
    