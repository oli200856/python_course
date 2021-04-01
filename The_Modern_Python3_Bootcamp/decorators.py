from functools import wraps

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM A WRAPPER FUNCTION"""
        print(f"You are about to call {fn.__name__}")
        print(f"Here are the docs: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

@log_function_data
def add(x,y):
        """Adds two numbers together"""
        return x + y

def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return "Invalid argument"
            return fn(*args, **kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_foods(*foods):
        print(foods)

fav_foods("burrito", "ice cream")
fav_foods("ice cream", "burrito")
