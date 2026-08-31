"""SOLUTION."""

class InvalidAgeError(Exception):
    pass


def read_age(raw: str) -> int:
    try:
        age = int(raw.strip())
    except ValueError as e:
        raise ValueError("age must be an integer") from e
    if age < 1 or age > 120:
        raise InvalidAgeError(f"age out of range: {age}")
    return age


if __name__ == "__main__":
    assert read_age("21") == 21
    try:
        read_age("abc")
    except ValueError:
        pass
    try:
        read_age("0")
    except InvalidAgeError:
        pass
    print("ok")
