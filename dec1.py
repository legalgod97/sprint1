import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return timer
    return wrapper

@timer
def my_function():
    return 386 ** 1000000

my_function()