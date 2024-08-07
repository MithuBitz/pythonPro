# Leap Year Checker

# Need to wrap inside a int() bcoz input return in string
year = int(input("Please enter the year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
    check = "Leap Year"
else :
    check = "Not Leap Year"


print(year,check)

