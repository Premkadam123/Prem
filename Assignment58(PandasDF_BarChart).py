"""
Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class.Also generate a bar chart based on the result and explain the conclusion.

 Input: student_data = pd.DataFrame({

 'school_code': ['s001','s002','s003','s001','s002','s004'], 

'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'], 

'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],

 'age': [12, 12, 13, 13, 14, 12], 'height': [173, 192, 186, 167, 151, 159], 

'weight': [35, 32, 33, 30, 31, 32],

 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )
 """

import pandas as pd
import matplotlib.pyplot as plt

# Creating the DataFrame with the provided student data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Grouping the data by 'class' and counting the number of students in each class
class_counts = student_data.groupby('class')['name'].count()

# Displaying the count of students per class
print("Number of students in each class:")
print(class_counts)

# Generating a bar chart based on the result
class_counts.plot(kind='bar', color='skyblue')

# Adding title and labels
plt.title('Number of Students per Class')
plt.xlabel('Class')
plt.ylabel('Number of Students')

# Displaying the bar chart
plt.show()


"""
Output:
Number of students in each class:
class
V     2
VI    4
Name: name, dtype: int64

Conclusion:
The bar chart shows that Class VI has the most students,
while Class V has fewer students.
This visualization helps in quickly understanding the distribution of students across different classes,
which can be useful for planning and resource allocation.
"""
