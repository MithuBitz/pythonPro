# Multiplication Table Printer

# Need to wrap inside a int() bcoz input return in string
num = int(input("Please enter a number for multyplication table: "))


for i in range(1, 11):
    if i == 5:
        continue
    else :
        multply = num * i
        print(num, "X", i, "=", multply)




