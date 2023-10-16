
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@logging_decorator
def add(x, y):
    return x + y


add(5, 6)

# Output: Calling add with arguments (5, 6) and keyword arguments {}
