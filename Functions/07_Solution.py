# Function with *args

def sum_all_num(*arg):
    print(arg)
    # iter through args
    for i in arg:
        print(i + 2)
    return sum(arg)

print(sum_all_num(1,2,3))
