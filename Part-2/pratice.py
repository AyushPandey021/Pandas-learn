import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Ayush", "Riya", "Kabir", "Sneha", "Rahul", "Anjali", "Vikram", "Priya"],
    "Age": [28, 25, 30, 24, 29, 27, 32, 26],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "IT", "Finance"],
    "Salary": [70000, 52000, 85000, 63000, 78000, 58000, 72000, 80000],
    "Experience_Years": [5, 2, 7, 3, 6, 3, 8, 4],
    "Status": [
        "Permanent",
        "Intern",
        "Permanent",
        "Contract",
        "Permanent",
        "Contract",
        "Permanent",
        "Permanent",
    ],
}

df = pd.DataFrame(data)

# ⭐ Task ⭐
# Print the first 5 rows of the dataset.

# Show only the Name and Salary columns.

# How many employees are in the dataset?

# 🔹 Filtering
# Get all employees from the Finance department.

# List employees with Salary > 70000.

# Find all female employees with more than 2 years of experience.

# 🔹 Grouping and Aggregation
# What is the average salary in each department?

# Find the total salary paid to Permanent employees.

# Count how many employees are there in each Department.

# 🔹 Sorting
# Sort employees by Experience_Years in descending order.

# Sort employees by Salary (highest to lowest) and show top 3.

# 🔹 New Column / Derived Data
# Create a new column called Tax which is 10% of the salary.

# Add a column called Seniority:

# 'Junior' if experience < 4 years

# 'Mid' if 4-6 years

# 'Senior' if > 6 years

# 🔹 Advanced
# What is the average experience of IT department employees?

# List the names of employees who are either Contract or Intern.

# Replace Status = "Intern" with "Trainee".

# print(df.head()) #task - 1⭐
# ok = df[["Name","Salary"]]  #task - 2 ⭐
# print(df["Employee_ID"].count()) #task - 3⭐
# print(df[df['Department']== "Finance"]) #task -4 ⭐
# print(df[df["Salary"]>70000]) #task -5 ⭐
# print( df[(df["Experience_Years"] > 2) & (df["Gender"] == "Female")]) # task - 6⭐️
# print(df.groupby("Department")["Salary"].mean()) #Task-7⭐
# print(df[df["Status"]== "Permanent"]["Salary"].mean()) # Task-8⭐
# print(df.groupby("Department").size()) #Task-9⭐
# print(df.sort_values(by="Experience_Years", ascending=False)) #Task-10⭐
# print(df.sort_values(by="Salary", ascending=False).tail(3))  # Task-11⭐
# tax_Column = df["Tax"] = df["Salary"] * 0.1
# print(tax_Column)
# print(df)  #task-12⭐
# def get_seniority(exp):
#     if exp < 4:
#         return 'Junior'
#     elif 4 <= exp <= 6:
#         return 'Mid'
#     else:
#         return 'Senior'

# df['Seniority'] = df['Experience_Years'].apply(get_seniority)
# print(df[['Name', 'Experience_Years', 'Seniority']]) #task-13⭐

# print(df[df['Department']== "IT"]["Experience_Years"].mean()) #Task-14 ⭐
# replace_Name=df['Status'] = df['Status'].replace('Intern', 'Trainee')
# print(replace_Name)  #task-15⭐
