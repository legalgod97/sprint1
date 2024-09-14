import time

def add_text(text):
    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            res = end - start
            print(f'{text} {res} секунд.')
            return res
        return wrapper
    return timer

@add_text('Функция выполнилась за')
def my_function():
    return 386 ** 1000000

my_function()