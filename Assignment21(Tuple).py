#Write a python program and iterate the given tuples Input: employee1 = ("John Doe", 101, "Human Resources", 60000) employee2 = ("Alice Smith", 102, "Marketing", 55000) employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Define tuples for employee records
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Create a list to store multiple employee records
employee_records = [employee1, employee2, employee3]

# Print employee records
print("Employee Records:")
for employee in employee_records:
    name, emp_id, department, salary = employee
    print(f"Name: {name}")
    print(f"Employee ID: {emp_id}")
    print(f"Department: {department}")
    print(f"Salary: ${salary}\n")


"""   OUTPUT=>
Employee Records:
Name: John Doe
Employee ID: 101
Department: Human Resources
Salary: $60000

Name: Alice Smith
Employee ID: 102
Department: Marketing
Salary: $55000

Name: Bob Johnson
Employee ID: 103
Department: Engineering
Salary: $75000

"""
