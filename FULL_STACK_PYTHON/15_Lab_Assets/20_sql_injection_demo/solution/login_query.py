"""SOLUTION — parameterized."""

def find_user(cursor, username: str):
    sql = "SELECT * FROM users WHERE username = %s AND active = 1"
    cursor.execute(sql, (username,))
    return cursor.fetchone()


def build_query_safe(username: str) -> tuple[str, tuple]:
    return ("SELECT * FROM users WHERE username = %s AND active = 1", (username,))


if __name__ == "__main__":
    sql, params = build_query_safe("admin' OR '1'='1")
    assert "%s" in sql and "OR" not in sql
    print(sql, params)
