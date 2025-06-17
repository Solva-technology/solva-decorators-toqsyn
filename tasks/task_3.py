from functools import wraps


def validate_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for x in args:
            if x <= 0:
                raise ValueError("Все аргументы должны быть положительными")
        return func(*args)

    return wrapper


@validate_positive
def multiply(a, b):
    return a * b
