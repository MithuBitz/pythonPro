import time
# Timing Function Execution
# Write a decorator that measures the time a function takes to execute.

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} run in {end-start} time")
        return result
    return wrapper

@timer # this is how we can declare a decorator after @ put the name of the function which we want to act as a decorator
def test_func(n):
    time.sleep(n)


test_func(2)