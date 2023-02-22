

def print_func_name(func):
    def incoming(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' well done. Result: {result}")
        return result
    return incoming


@print_func_name
def add(a, b):
    return a + b


@print_func_name
def multiply(a, b):
    return a * b


print(add(2, 3))
print(multiply(2, 3))
