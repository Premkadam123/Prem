#1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).
#Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

#import requried liabrary
import numpy as np

# Given input
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35 degrees Celsius)
hot_day_indices = np.where(temperatures > 35)

# Identify cold days (temperature < 35 degrees Celsius)
cold_day_indices = np.where(temperatures < 35)

# Print the table header
print(f"{'Hot Days'}")
print(f"{'Day    '}{'Temperature (°C)'}")

# Print hot days
for index in hot_day_indices[0]:
    print(f"{index}{temperatures[index]:>15}")

# Print the table header
print(f"{'Cold Days'}")
print(f"{'Day    '}{'Temperature (°C)'}")

# Print cold days
for index in cold_day_indices[0]:
    print(f"{index}{temperatures[index]:>15}")


#output:

#Hot Days
#Day    Temperature (°C)
#2           36.8
#5           38.7
#9           37.2
#Cold Days
#Day    Temperature (°C)
#0           32.5
#1           34.2
#3           29.3
#4           31.0
#6           23.1
#7           18.5
#8           22.8
