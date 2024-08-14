# Debugging Function Calls
# Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        arg_value = ", ".join(str(arg) for arg in args)
        kwarg_value = ", ".join(f"{k}={v}" for k,v in kwargs.items())
        print(f"Calling: {func.__name__} with args {arg_value} and kwargs {kwarg_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def greet(name, greetings="Namashkar"):
    print(f"{greetings} {name}")

greet("Niranjan")
greet("Anurag", greetings="Wao!")
