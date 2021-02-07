"""An example of a function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest arguement."""
    if a >= b:
        return a
        else:
            return b

print(my_max(10+1, 10))

