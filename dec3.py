import datetime

def log_function(filename):
    def dec(func):
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f'Function: {func.__name__}\n')
                file.write(f'Arguments: {', '.join([str(i) for i in args])}\n')
                file.write(f'Result: {func(*args, **kwargs)}\n')
                file.write(f'Timestamp: {timestamp}')
            return log_function
        return wrapper
    return dec


@log_function("log.txt")
def calc_add(a, b):
    return a + b

calc_add(1, 2)