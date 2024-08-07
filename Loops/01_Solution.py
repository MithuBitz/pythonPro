# Counting Positive Numbers

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
print("Number List: ", numbers)

count_positive_num = 0

for num in numbers :
    if num > 0 :
        count_positive_num += 1


print("There are ", count_positive_num, "positive number in the numbers list")