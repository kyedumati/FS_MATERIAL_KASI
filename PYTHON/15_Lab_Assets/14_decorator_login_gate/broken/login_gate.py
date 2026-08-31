"""BROKEN decorator."""

current_user = None


def require_login(func):
    # Bug: calls func immediately at decoration time
    if current_user is None:
        print("Access denied")
        return func
    return func


@require_login
def view_salary():
    print(f"Salary slip for {current_user}")


if __name__ == "__main__":
    view_salary()
