# Scope

name = "Mithu"

def fun():
    # name = "Niranjan"
    print(name)

# print(name)
# fun() 

# In local scope if a variable is not found then it check for that variable in their outer scope

# Value pic from global to local
num1 = 11

def fun1(num2):
    total = num1 + num2
    return total

def fun2():
    # global name # ITs a very bad practice to change the global value
    name = "Khukhu"
    return name

def fun3():
    name = "Sachin" # If it is comment out then name is access from global by fun4()
    def fun4():
        print(name)
    # fun4()
    return fun4

fun3()
result = fun3()
result() # This is called Clouser
# result not only return the fun4() but also all variable and everything holds in result

# print(fun1(11))

# print(name)
# print(fun2())
