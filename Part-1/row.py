# head()
# head return top rows
# tail()
# tails retun bottom rows
# import pandas as pd

# # Use correct path to the file
# df = pd.read_csv(
#     "C:/Users/vloga/OneDrive/Desktop/Numpy/Pandas/sales_data.csv", encoding="latin1"
# )
# print("Display the 5 rows in data top🔝")
# print(df.head(2))


# # df.head(2)
# print("Display 5 rows in list in bottom↙️")
# print(df.tail(2))


# task 2⏭️

import pandas as pd

data = {
    "Name": [
        "Ram",
        "Shyam",
        "Ganesh",
        "krish",
        "Somu",
        "kittu",
        "Ashish",
        "Vinayka",
        "Sruti",
        "Vaibhav",
    ],
    "Age": [43, 25, 30, 40, 41, 45, 23, 42, 28, 26],
    "Salary": [60000, 60000, 40000, 35000, 40000, 23000, 54000, 74000, 32000, 21000],
    "Performance_Score": [85, 90, 32, 45, 75, 76, 87, 78, 97, 56],  # fixed here
}
# Access row by index

df = pd.DataFrame(data)


# Employees with salary > 50000
highSalary = df[df["Salary"] > 50000]
print("Employees with salary > 50000")
print(highSalary)

# Filter rows: Age > 30 and Salary > 50000
filter = df[(df["Age"] > 30) & (df["Salary"] > 50000)]
print("\nEmployees with Age > 30 and Salary > 50000")
print(filter)

# Using OR condition: Age > 35 or Performance Score > 90
filteror = df[(df["Age"] > 35) | (df["Performance_Score"] > 90)]
print("\nEmployees older than 35 or Performance Score > 90")
print(filteror)


