"""STARTER — exceptions. Finish read_age. No type hints."""

class InvalidAgeError(Exception):
    pass


def read_age(raw):
    # TODO: int() in try; InvalidAgeError if not 1–120
    raise NotImplementedError


if __name__ == "__main__":
    for sample in ["21", "abc", "0", "200"]:
        try:
            print(sample, "->", read_age(sample))
        except Exception as e:
            print(sample, type(e).__name__, e)
