import functools

user = {"name": "Damian K", "permission": "admin"}


# Decorator
def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["permission"] == "admin":
            return func(*args, **kwargs)
        else:
            return "No admin rights"

    return secure_function


@make_secure
def get_admin_password(panel):
    if panel == "billing":
        return "1234"
    else:
        return "5678"


print(get_admin_password("billings"))
