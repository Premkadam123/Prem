#Lab 1: Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
#Input:Download the file salesdata.csv From LMS Output:


#import pandas and numpy liabrary
import pandas as pd
import numpy as np

#read the salesdata csv file
df=pd.read_csv("C:\\Users\Kiran\Downloads\salesdata.csv")

#display the pivot table
pd.pivot_table(df,index=["Region","Manager","SalesMan"],values=["Sale_amt"],aggfunc=np.sum)

#output:
#			                        Sale_amt
#Region	    Manager	  SalesMan
#Central	Douglas	    John	    124016.0
#           Hermann	    Luis	    206373.0
#                       Shelli	    33698.0
#                       Sigal	    125037.5
#           Marth	    Steven	    14000.0
#           Martha	    Steven	    185690.0
#           Timothy	    David	    140955.0
#East	    Douglas	    Karen	    48204.0
#           Martha	    Alexander	236703.0
#                       Diana	    36100.0
#West	    Douglas     Michael	    66836.0
#           Timothy	    Stephen	    88063.0


