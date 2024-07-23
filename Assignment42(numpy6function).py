#2.Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis.
#Input: # Employee data for full-time employees
 #full_time_employees = np.array([
 #[101, 'John Doe', 'Full-Time', 55000],
 #[102, 'Jane Smith', 'Full-Time', 60000],
 #[103, 'Mike Johnson', 'Full-Time', 52000]
 #])
 # Employee data for part-time employees :
 #part_time_employees = np.array([
 #[201, 'Alice Brown', 'Part-Time', 25000],
 #[202, 'Bob Wilson', 'Part-Time', 28000],
 #[203, 'Emily Davis', 'Part-Time', 22000]
 #])


#import requried liabrary
import numpy as np

# Given input: Employee data for full-time employees
full_time_employees = np.array ([

 [101, 'John Doe', 'Full-Time', 55000],

 [102, 'Jane Smith', 'Full-Time', 60000],

[103, 'Mike Johnson', 'Full-Time', 52000]

])

#Given input: Employee data for part-time employees
part_time_employees = np.array([

[201, 'Alice Brown', 'Part-Time', 25000],

[202, 'Bob Wilson', 'Part-Time', 28000],

 [203, 'Emily Davis', 'Part-Time', 22000]

 ])
#concatenate the both array in one
combined_employee_data = np.concatenate((full_time_employees,part_time_employees),axis=0)
#print the combined employee data
print("Combined Employee Data:")
for employee in combined_employee_data:
    print(f"Employee ID:{employee[0]},Name:{employee[1]},Type:{employee[2]},Salary:{employee[3]}")


 #output:
#Combined Employee Data:
#Employee  ID: 101, Name: JohnDoe, Type: Full - Time, Salary: 55000
#EmployeeID: 102, Name: JaneSmith, Type: Full - Time, Salary: 60000
#EmployeeID: 103, Name: MikeJohnson, Type: Full - Time, Salary: 52000
#EmployeeID: 201, Name: AliceBrown, Type: Part - Time, Salary: 25000
#EmployeeID: 202, Name: BobWilson, Type: Part - Time, Salary: 28000
#EmployeeID: 203, Name: EmilyDavis, Type: Part - Time, Salary: 22000

 