# sorting for the data management and sequence the linear form your 
# arenge the data rows and column

# sorting data in one column
# Sorting data syntax⏭️
# df.sort_values(by="ColumnName",ascending=True/False,inplace=True)

import pandas as pd
data = {
"Name":["Kittu","zyan","APdev","lokesh"],

"age":[23,24,33,43],
"Salary":[10000,24000,43000,34000]
}
df = pd.DataFrame(data)
#  this mathod to use in single coloumn and set acending and dacending
df.sort_values(by="Name",ascending=True,inplace=True)
print("Sort Name data by Alfabet aescending")
print(df)