def timing(func):
    # Bug: mutable default / wrong — calls func at decoration time conceptually broken
    def wrapper(*args, history=[]):
        history.append(func.__name__)
        return func(*args)
    return wrapper
