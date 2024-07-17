"""Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11   """

str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print("Original strings : ",str)
upr, lwr, num, spl = 0, 0, 0, 0
for i in range(len(str)):
	if str[i] >= 'A' and str[i] <= 'Z':
		upr += 1
	elif str[i] >= 'a' and str[i] <= 'z':
		lwr += 1
	elif str[i] >= '0' and str[i] <= '9':
		num += 1
	else:
		spl += 1
 
print("UpperCase : ",upr)
print("LowerCase : ",lwr)
print("NumberCase : ",num)
print("SpecialCase : ",spl)



""" outout=>
Original strings :  Hell0 W0rld ! 123 * # welcome to pYtHoN
UpperCase :  5
LowerCase :  18
NumberCase :  5
SpecialCase :  11

"""
