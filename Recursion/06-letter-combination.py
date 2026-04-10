def letter_combination(digits:str):
    digit_to_letters = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    result=[]
    
    def helper(index:int, current_combination:str):
        
        if index == len(digits):
            result.append(current_combination)
            return
        current_digit=digits[index]
        letters = digit_to_letters[current_digit]
        for letter in letters:
            helper(index+1,current_combination+letter)
    helper(0,"")
    return result
dts='234'
r=letter_combination(dts)
print(f"value of result is {r}")

        
        