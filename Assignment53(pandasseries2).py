
#2: Suppose you want to track and analyze your household expenses for a month. You have recorded the expenses for various categories, such as groceries, utilities, rent, transportation, and entertainment. You can represent this expense data using a Pandas Series.
#Input: # Expense categories
#categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
# Monthly expense data (example data in USD)
#expenses = [500, 200, 1200, 300, 150]


#import pandas liabrary
import pandas as pd
#given data
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]
#create the pandas series
series = pd.Series(expenses,categories)
#print the series
print(series)


#output:
#Groceries          500
#Utilities          200
#Rent              1200
#Transportation     300
#Entertainment      150
#dtype: int64