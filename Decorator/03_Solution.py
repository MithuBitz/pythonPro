import time
# Cache Return Values
# Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.

#decorator fuction
def cache(func):
    # Variable to store the cache result
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            print(cache_value)
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def sum_of_nums(a, b):
    time.sleep(2)
    return a + b

print(sum_of_nums(2,5))

print(sum_of_nums(2,5))

print(sum_of_nums(3,5))
