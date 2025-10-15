def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        return s
    return s[::-1]
    

# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
result1 = string_reverse("Hello World")
print(result1)  # Expected: "dlroW olleH"
# - "Python"
result2 = string_reverse("Python")
print(result2)  # Expected: "nohtyP"
