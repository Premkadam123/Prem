# Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time. You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.

# Input: months = np.arange(1, 13) 

# electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) 

# clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) 

# home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])

# sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Data for the sales performance comparison
months = np.arange(1, 13)
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Plotting the pie chart
plt.figure(figsize=(8, 4))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Monthly Income by Source')
plt.axis('equal')
plt.show()

# Plotting the sales performance comparison
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(months, electronics_sales, marker='o')
plt.title('Electronics Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(months, clothing_sales, marker='o', color='orange')
plt.title('Clothing Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(months, home_garden_sales, marker='o', color='green')
plt.title('Home & Garden Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(months, sports_outdoors_sales, marker='o', color='red')
plt.title('Sports & Outdoors Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)

plt.tight_layout()
plt.show()
