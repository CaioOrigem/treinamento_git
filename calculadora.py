def soma(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("Both arguments must be numbers.")
    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")
    return a + b