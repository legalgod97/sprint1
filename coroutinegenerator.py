def my_coroutine():
    yield 1
    yield 2
    yield 3

coroutine = my_coroutine()

value1 = next(coroutine)
value2 = next(coroutine)
value3 = next(coroutine)


try:
    next(coroutine)
except StopIteration:
    pass
