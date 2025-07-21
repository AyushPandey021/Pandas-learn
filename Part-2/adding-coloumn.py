# adding coloum 

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

# adding columns
# symtax = brakecets df["Colums_Name"= some_Data
df = pd.DataFrame(data)
print(df)
# adding new column and add the value also 
df["Bonus"] = df["Salary"] *2
print(df)

#using insert
#df.insert(loc,"Coloum-name","some-data")
df.insert(0,"Employee-ID",[10,20,30,40,50,60,70,80,90,100])

print(df)

