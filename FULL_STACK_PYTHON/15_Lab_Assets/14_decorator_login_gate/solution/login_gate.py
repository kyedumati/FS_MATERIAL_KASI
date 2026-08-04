"""SOLUTION — login-gate decorator (no functools.wraps required)."""

current_user = None


def require_login(func):
    def wrapper(*args, **kwargs):
        if current_user is None:
            print("Access denied. Please login first.")
            return None
        return func(*args, **kwargs)

    return wrapper


@require_login
def view_salary():
    print(f"Salary slip for {current_user}")


def login(name):
    global current_user
    current_user = name


if __name__ == "__main__":
    view_salary()
    login("Anita")
    view_salary()
