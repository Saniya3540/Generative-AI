#---------Assignment of Decorator---------

'''1. Develop a memoization decorator that caches the results of function
calls and returns the cached result when the same inputs occur again.
This can greatly improve the performance of recursive or
computationally intensive functions.'''

def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper


@memoize
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
