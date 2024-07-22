#1. Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
try:
  with open("D:\\Demo\\abc.txt", 'r') as file:
   for line in file:
    print(line, end='')  # Using end='' to avoid adding extra newlines
except FileNotFoundError:
  print(f"The file abc.txt does not exist.")


#output
#Hi Virat, This is append text, how are u.
#This is append text, how are u

S