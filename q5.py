def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return "num or divisor is / are not numeric"
    if divisor == 0:
        return "divisor cannot be zero"
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
result1 = check_divisibility(-10, 2)
print(result1)  # Expected: True (since -10 % 2 == 0)

# - 7, 3
result2 = check_divisibility(-7, 3)
print(result2)  # Expected: False (since -7 % 3 == -1)
