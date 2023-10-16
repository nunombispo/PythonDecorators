def authorization_decorator(func):
    def wrapper(user):
        if user.is_authorized:
            return func(user)
        else:
            print("User not authorized")

    return wrapper


class User:
    def __init__(self, is_authorized):
        self.is_authorized = is_authorized


@authorization_decorator
def sensitive_function(user):
    print("Access granted to sensitive data")


user1 = User(is_authorized=True)
sensitive_function(user1)
# Output: Access granted to sensitive data

user2 = User(is_authorized=False)
sensitive_function(user2)
# Output: User not authorized
