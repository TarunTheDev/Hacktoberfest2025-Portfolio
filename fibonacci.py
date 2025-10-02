def fibonacci(limit: int):
    """
    Generate Fibonacci numbers up to a given limit.
    Example:
        list(fibonacci(10)) -> [0, 1, 1, 2, 3, 5, 8]
    """
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b


# Demo usage
if __name__ == "__main__":
    print(list(fibonacci(20)))
    # Output: [0, 1, 1, 2, 3, 5, 8, 13]
