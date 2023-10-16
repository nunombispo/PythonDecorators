

def decorator_one(func):
    def wrapper():
        print("Decorator one engaged!")
        func()
    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator two engaged!")
        func()
    return wrapper


@decorator_one
@decorator_two
def my_function():
    print("Original function executed.")


my_function()

# Output:
# Decorator one engaged!
# Decorator two engaged!
# Original function executed.

