# Basic Function Syntax

# in python function is called as defination or def

def square_of_num(num): # Here num is called parameter
    # result = num ** 2
    # print("Square of ", num, "is : ", result) 
    # Its a bad practice to print in function def so we use return
    return num ** 2


result = square_of_num(4)
print(result)
