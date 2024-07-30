#1. Install matplotlib  & you can use plt.plot() to create a line plot of given data
#x = [0, 5, 9, 10, 15, 20, 25]
#y = [0, 1, 2, 3, 4, 5, 6]


#import requried library
import matplotlib.pyplot as plt

# Given data
x = [0, 5, 9, 10, 15, 20, 25]

y = [0, 1, 2, 3, 4, 5, 6]

#create a line plot
plt.plot(x,y)

#add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")

#show the plot
plt.show()

#output:
