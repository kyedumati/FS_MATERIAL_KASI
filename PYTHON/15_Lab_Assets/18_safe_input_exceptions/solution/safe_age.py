"""SOLUTION — MedCare safe age. No type hints. No exception chaining."""

class InvalidAgeError(Exception):
    pass


def read_age(raw):
    try:
        age = int(raw.strip())
    except ValueError:
        raise ValueError("age must be an integer")
    if age < 1 or age > 120:
        raise InvalidAgeError(f"age out of range: {age}")
    return age


if __name__ == "__main__":
    for sample in ["21", "abc", "0", "200"]:
        try:
            print(sample, "->", read_age(sample))
        except Exception as e:
            print(sample, type(e).__name__, e)
