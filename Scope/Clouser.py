# CLouser in Python explain by a programm

def cube_finder(num):
    def inside_fun(a):
        return a ** num
    return inside_fun

cube_of_three = cube_finder(3)
cube_of_two = cube_finder(2)

# cube_finder() function also holds the insider_fun() and its value
print(cube_of_three(3))
print(cube_of_two(3))