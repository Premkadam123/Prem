#Write a Python script to concatenate the following dictionaries to create a new one.

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating dictionaries
result = {**dic1, **dic2, **dic3}

# Printing the result
print("Resulting Dictionary:", result)

#OUTPUT

Resulting Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
