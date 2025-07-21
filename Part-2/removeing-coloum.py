# data
#
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
    "Performance_Score": [85, 90, 32, 45, 75, 76, 87, 78, 97, 56],  #fixed here
}
df = pd.DataFrame(data)
print(df)
# drop the data means remove
# syntax = df.drop(colums = ["colums-name"],inplace = True)
print("Modified data Removing performence-column Removed❌")
# removeing one  column 
df.drop(columns=["Performance_Score"], inplace=True)
# removeing multiple column column 
# syntax are same  add columns name
# df.drop(columns=["Performance_Score","Age","Name"], inplace=True)
print(df)
