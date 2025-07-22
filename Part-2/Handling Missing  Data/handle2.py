#dropna()
import pandas as pd
data = {
    "Name": [
        "Ram",
        None,
        "Shyam",
        "krish",
        "Somu",
        "kittu",
        "Ashish",
        "Vinayka",
        "Sruti",
        "Vaibhav",
    ],
    "Age": [43, None, 30, 40, 41, 45, 23, 42, 28, 26],
    "Salary": [60000, None, 40000, 35000, 40000, 23000, 54000, 74000, 32000, 21000],
    "Performance_Score": [85, None , 32, 45, 75, 76, 87, 78, 97, 56],  # fixed here
}

df = pd.DataFrame(data)
print(df)


# df.fillna(0,inplace= True)
# fillna for fill the data 
# df['Age'].fillna(df['Age'].mean(),inplace=True)
# df['Salary'].fillna(df['Salary'].mean(),inplace=True)
# df['Performance_Score'].fillna(df['Performance_Score'].mean(),inplace=True)
 

#  fill the missing data ⏭️
df["Name"].fillna("Ayush", inplace=True)
df["Age"].fillna(23,inplace=True)
df["Salary"].fillna(35000,inplace=True)



print(df)






