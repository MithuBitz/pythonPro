# Find the First Non-Repeated Character from a String

input_str = input("Please enter a String: ")

for char in input_str :
    if input_str.count(char) == 1 :
        print("The First non-repeated Charecter is : ", char)
        # To optimize the code 
        # use break so that when first char is found exit the loop
        break
        
    

