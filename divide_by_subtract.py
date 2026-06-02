from subtract import subtract

def divide(a, b):
    # 1. Type validation
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")

    # 2. Prevent division by zero
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")

    # 3. Core subtraction loop
    count = 0
    while a >= b:
        a = subtract(a, b)  # Subtract b from a using your function
        count += 1          # Keep track of how many times we subtracted
        
    return count