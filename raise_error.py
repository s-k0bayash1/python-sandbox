def main():
    try:
        raise_error()
    except Exception as e:
        CustomError(e)


def raise_error():
    raise ValueError("value error")


class CustomError(Exception):
    def __init__(self, e):
        super(f"error is {e}")


if __name__ == "__main__":
    main()
