# List Uniqueness Checker

items = ["apple", "banana", "orange", "apple", "mango"]

# set only include unique number
unique_item = set()

for item in items :
    if item in  unique_item:
        print("Duplicate")
        break
    unique_item.add(item)

