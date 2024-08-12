# Function with **kwargs
# Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def key_value_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


key_value_args(name="Niranjan", location="India")

key_value_args(name="Anurag")

key_value_args(name="Mithu", loc="Indian", gender="Male")