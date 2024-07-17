""" Write a Python Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are:8  """

# count vowels in a string

# declare, assign string
str = "Welcome to Python Assignment"

# declare count
count = 0

# iterate and check each character
for i in str:
    # check the conditions for vowels
    if (
        i == "A"
        or i == "a"
        or i == "E"
        or i == "e"
        or i == "I"
        or i == "i"
        or i == "O"
        or i == "o"
        or i == "U"
        or i == "u"
    ):
        count += 1

# print count
print("Total vowels are: ", count)

"""output=>

Total vowels are:  8  """
