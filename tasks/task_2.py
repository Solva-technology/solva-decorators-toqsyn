from functools import wraps


def simple_cache(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = args
        if key in cache:
            print("Из кэша")
            return cache[key]
        result = func(*args)
        cache[key] = result
        return result

    return wrapper


@simple_cache
def add(a, b):
    return a + b
