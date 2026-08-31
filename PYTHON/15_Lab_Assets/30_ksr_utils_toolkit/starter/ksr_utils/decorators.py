_token = None


def set_token(token):
    global _token
    _token = token


def timing(func):
    # TODO: wrap with time.perf_counter; print elapsed seconds with func.__name__; return result
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def require_token(func):
    # TODO: if _token is None, print Access denied and return None; else call func
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
