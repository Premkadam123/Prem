#2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#Input: my_list = [1, 2, 3, 4, 5]

#import numpy liabrary
import numpy as np
# Define the list
my_list = np.array([1,2,3,4,5])
# Display the first and last index
first_index = 0
last_index = len(my_list) - 1
print("First index:", first_index)
print("Last index:", last_index)

# Multiply each element by 2
new_list = my_list * 2
# print the result
print("New array:",new_list )


#output
#First index: 0
#Last index: 4
#New array: [ 2  4  6  8 10]