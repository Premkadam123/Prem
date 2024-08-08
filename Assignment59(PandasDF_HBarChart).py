"""
Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.

 Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],

 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 

'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 

'age': [12, 12, 13, 13, 14, 12], 

'height': [173, 192, 186, 167, 151, 159], 

'weight': [35, 32, 33, 30, 31, 32], 

'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )
"""

import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame with the provided student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Grouping the data by 'school_code' and calculating mean, min, and max for 'age'
school_age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Displaying the statistics for each school
print("Mean, Min, and Max age for each school:")
print(school_age_stats)

# Generating a horizontal bar chart for the mean age
school_age_stats['mean'].plot(kind='barh', color='lightgreen', edgecolor='black')

# Adding title and labels
plt.title('Mean Age of Students by School Code')
plt.xlabel('Mean Age')
plt.ylabel('School Code')

# Displaying the horizontal bar chart
plt.show()


"""
Output:
Mean, Min, and Max age for each school:
             mean  min  max
school_code                
s001         12.5   12   13
s002         13.0   12   14
s003         13.0   13   13
s004         12.0   12   12


Conclusion:
The bar chart shows that the average age of students varies slightly across different schools.
Schools s002 and s003 have a higher average age (13 years), indicating that they might have older students on average.
School s004 has the lowest average age of 12 years, suggesting it has a younger student population.
"""
