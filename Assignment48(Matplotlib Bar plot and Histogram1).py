# Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

# Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

# expenses = [1200, 400, 200, 150, 250]

import matplotlib.pyplot as plt

# Data for monthly expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create a bar chart
plt.bar(categories, expenses, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Monthly Expenses by Category')
plt.xlabel('Category')
plt.ylabel('Expenses in Dollars')

# Show the plot
plt.show()
