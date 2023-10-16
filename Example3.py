

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class-based decorator engaged!")
        self.func(*args, **kwargs)


@MyDecorator
def say_goodbye():
    print("Goodbye!")


say_goodbye()

# Output:
# Class-based decorator engaged!
# Goodbye!
