import logging
import functools

#set up logging
logging.basicConfig(level=logging.INFO)

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Calling {func.__name__} with {args}, {kwargs}')
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        return result
    return wrapper

@log_calls
def add(x, y):
    return x + y

result = add(3, 9)
print(result) # Output: 12
