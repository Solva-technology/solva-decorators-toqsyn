from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ", ".join(repr(arg) for arg in args)
        print(f"Вызов: {func.__name__}({args_str})")
        result = func(*args, **kwargs)
        print("Результат: " + str(result))
        return result

    return wrapper


@log
def add(a, b):
    return a + b
