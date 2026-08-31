import time

_token = None


def set_token(token):
    global _token
    _token = token


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"[TIMER] {func.__name__}: {time.perf_counter() - start:.4f}s")
        return result

    return wrapper


def require_token(func):
    def wrapper(*args, **kwargs):
        if _token is None:
            print("Access denied")
            return None
        return func(*args, **kwargs)

    return wrapper
