#2: Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}


#import pandas and numpy liabrary
import pandas as pd
import numpy as np

#given sample data dictioary
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}

#display the data frame
df= pd.DataFrame(exam_data)
df

#output
    #name	    score	attempts   qualify
#	Anastasia	12.5	1	        yes
#1	Dima	    9.0	    3	        no
#2	Katherine	16.5	2	        yes
#3	James	    NaN	    3	        no
#4	Emily	    9.0	    2	        no
#5	Michael	    20.0	3	        yes
#6	Matthew	    14.5	1	        yes
#7	Laura	    NaN	    1	        no
#8	Kevin	    8.0	    2	        no
#9	Jonas	    19.0	1	        yes