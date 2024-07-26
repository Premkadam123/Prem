#2.Calculate the profit made by a company
#Input: revenue = np.array([10000, 12000, 11000, 10500])
#expenses = np.array([4000, 5000, 4500, 4800])
#Output: Profit: [6000 7000 6500 5700]

#import requried liabray
import numpy as np

#given input
revenue = np.array([10000, 12000, 11000, 10500])

expenses = np.array([4000, 5000, 4500, 4800])

#calculate the profit made by company
profit = revenue - expenses

#print the output
print("Profit:",profit)

#output:
#Profit: [6000 7000 6500 5700]