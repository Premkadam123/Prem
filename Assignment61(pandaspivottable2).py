# Lab 2: Write a Pandas program to create a Pivot table and find the item wise unit sold.
#Input:Download the file salesdata.csv From LMS


#import pandas and numpy liabrary
import pandas as pd
import numpy as np

#read the salesdata csv file
df=pd.read_csv("C:\\Users\Kiran\Downloads\salesdata.csv")

#display the pivot table
pd.pivot_table(df,index=["Item"],values=["Units","Sale_amt"],aggfunc=np.sum)




#output:
#	           Sale_amt   Units
#Item
#Cell Phone	   62550.0	  278
#Desk	       1250.0	  10
#Home Theater  361000.0	  722
#Television	   857768.0	  716
#Video Games   23107.5	  395
