
#Python program to check if the given string is a palindrome
# given string
given_string = "aassaa"
 
# an empty string variable to store
# the given string in reverse
reverse_string = ""
 
# iterate through the given string
# and append each element of the given string
# to the reverse_string variable
for i in given_string:
    reverse_string = i + reverse_string  
 
# if given_string matches the reverse_srting exactly
# the given string is a palindrome
if(given_string == reverse_string):
   print("The string", given_string,"is a Palindrome.")
 
# else the given string is not a palindrome   
else:
   print("The string",given_string,"is NOT a Palindrome.")

""" output=>

The string aassaa is a Palindrome.  """
