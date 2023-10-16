import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper


@timing_decorator
def slow_function(duration):
    time.sleep(duration)


slow_function(3)

# Output: Execution time: 3.0001230239868164 seconds
