import pandas as pd
data = {
"Name":["Kittu","zyan","APdev","lokesh","Trun ", "Karun ","Trun","Yash"],

"Age":[23,24,33,43,32,21,32,23],
"Salary":[10000,24000,43000,34000,14000,35000,42000,48000]
}
df = pd.DataFrame(data)
grouped = df.groupby(["Age","Name"])["Salary"].sum()

print(grouped)
# createing one group of Age and Salary
#  grup the data and performing aggregation in data-set
"""  
dr.groupby("Age")
age = 21> [35000]
age = 23 [10000,48000]
age = 24 [24000]
age = 32 [14000,42000]

[Salary].sum()

"""