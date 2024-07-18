# Write a Python program to sum all the items in a list.
def sum_list(items):
    total = 0
    for item in items:
        total += item
    return total

# Example usage
numbers = [1, 2, 3, 4, 5]
print("Sum of all items in the list:", sum_list(numbers))

# Output : Sum of all items in the list: 15