"""BROKEN — injectable."""

def find_user_sql(username: str) -> str:
    return f"SELECT * FROM users WHERE username = '{username}' AND active = 1"


if __name__ == "__main__":
    print(find_user_sql("admin' -- "))
