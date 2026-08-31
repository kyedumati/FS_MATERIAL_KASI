"""STARTER — use parameterized queries (API sketch)."""

def build_query_unsafe(username: str) -> str:
    # DO NOT USE — shown for contrast
    return f"SELECT * FROM users WHERE username = '{username}'"


def build_query_safe(username: str) -> tuple[str, tuple]:
    # TODO: return (sql_with_%s, (username,))
    raise NotImplementedError


if __name__ == "__main__":
    attack = "admin' OR '1'='1"
    print("unsafe:", build_query_unsafe(attack))
    print("safe:", build_query_safe(attack))
