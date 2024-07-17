# Write a python program finding the factorial of a given number using a while loop.

num = int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
    fac = fac * i
    i = i + 1
 
print("factorial of ", num, " is ", fac)

""" OUTPUT=>
enter a number: 5
factorial of  5  is  120
"
