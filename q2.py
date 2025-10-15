def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list):
        return lst
    return [replace_val if x == find_val else x for x in lst]
    

# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Scenario 1: [1, 2, 3, 4, 2, 2] -> find 2 and replace with 5
result1 = find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
print(result1)  # Expected: [1, 5, 3, 4, 5, 5]

# Scenario 2: ["apple", "banana", "apple", "apple", "orange"] -> find "apple" and replace with "orange"
result2 = find_and_replace(["apple", "banana", "apple", "apple", "orange"], "apple", "orange")
print(result2)  # Expected: ["orange", "banana", "orange", "orange", "orange"]
