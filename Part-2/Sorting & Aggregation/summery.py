""" Aggregation
aggregation mathod help and performing mathametical equation in data set 
 df["Coloumn Name"].sum()
df["coloum Name"].mean()
min()
max()
"""



import pandas as pd 
data = {
"Name":["Kittu","zyan","APdev","lokesh"],

"Age":[23,24,33,43],
"Salary":[10000,24000,43000,34000]
}

df = pd.DataFrame(data)
paisa = df["Salary"].sum()



print("Mean of the Age is ",paisa)
print(df)
