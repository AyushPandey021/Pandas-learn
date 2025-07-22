# this is sorting in multi rows and coloums
# syntax⏭️
# df.sort_values(by=["Age","Salary"],ascending= True,inplace= True)
import pandas as pd
data = {
"Name":["Kittu","zyan","APdev","lokesh"],

"Age":[23,24,33,43],
"Salary":[10000,24000,43000,34000]
}
df = pd.DataFrame(data)

df.sort_values(by=["Name","Age"],ascending=[False,True],inplace=True)
#  if selact the multi coloumn  and each coloum add condition true or false. 
print("Sort Name, Age column")
print(df)