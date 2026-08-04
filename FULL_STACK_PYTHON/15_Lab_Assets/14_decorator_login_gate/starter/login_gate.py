"""STARTER — write require_login decorator."""

current_user = None


def require_login(func):
    # TODO: wrapper checks current_user; if None print message else call func
    def wrapper(*args, **kwargs):
        pass

    return wrapper


@require_login
def view_salary():
    print(f"Salary slip for {current_user}")


if __name__ == "__main__":
    view_salary()
    current_user = "Anita"
    view_salary()
