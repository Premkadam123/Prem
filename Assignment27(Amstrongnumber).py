# Python program to check if a given number is an Armstrong number

# the given number
given_number = 153
 
# convert given number to string
# so that we can iterate through it
given_number = str(given_number)
 
# store the lenght of the string for future use
string_length = len(given_number)
 
# initialize a sum variable with
# 0 value to store the sum of the product of
# each digit
sum = 0
 
# iterate through the given string
for i in given_number:
    sum += int(i)**string_length
 
# if the sum matches the given string
# its an amstrong number
if sum == int(given_number):
    print("The given number",given_number,"is an Amstrong number.")
 
# if the sum do not match with the given string
# its an amstrong number
else:
    print("The given number",given_number,"is Not an Amstrong number.")

""" output=>

The given number 153 is an Amstrong number.    """
