# Problem 39: Merge two dictionaries
# Find and fix the error

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged = dict1.copy()  # make a copy so dict1 stays unchanged
merged.update(dict2)   # add items from dict2

print(f"Merged dictionary: {merged}")
