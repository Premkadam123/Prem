#2.Compute the standard deviation of the NumPy array Input: arr = [20, 2, 7, 1, 34]

#import requried liabray
import numpy as np
#given input
arr = [20, 2, 7, 1, 34]
#calculate standard deviation
std_value=np.std(arr)
#calculate more precision with float32
more_precision=np.std(arr,dtype=np.float32)

#calculate more accuracy with float64
more_accuracy=np.std(arr,dtype=np.float64)
#print the output
print("The standard deviation of the array is:",std_value)
print("The standard deviation more precision of the array is:",more_precision)
print("The standard deviation more accuracy of the array is:",more_accuracy)

#output:

#The standard deviation of the array is: 12.576167937809991
#The standard deviation more precision of the array is: 12.576168
#The standard deviation more accuracy of the array is: 12.576167937809991