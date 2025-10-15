def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print(f"Original value for {key}: {dct[key]}")
    dct[key] = value
    return dct
   


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
dict1 = {"name": "Alice"}
result1 = update_dictionary(dict1, "age", 25)
print(result1)  # Expected: {'name': 'Alice', 'age': 25}

# - {"age": 25}, "age", 26
dict2 = {"age": 25}
result2 = update_dictionary(dict2, "age", 26)
print(result2)  # Expected: Original value for age: 25, then {'age': 26}