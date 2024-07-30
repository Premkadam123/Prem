# Visualize the daily temperature changes over time in a city and give your conclusion

#Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

# temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

import matplotlib.pyplot as plt

# Data for daily temperature
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create a line chart
plt.plot(days, temperature, marker='o', linestyle='-', color='b')

# Add title and labels
plt.title('Daily Temperature Changes Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature in °F')

# Show the plot
plt.grid(True)
plt.show()
