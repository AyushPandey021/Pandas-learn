# Updateing Value

# data
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
df = pd.DataFrame(data)
print(df)

df.loc[0,'Salary'] = 95000
print(df)
# 2nd updateing is updateing a full coloum value on data means all indexes are updates in coloum

#increseing salart by 3%
df.loc[9,'Salary'] = 50000
df['Salary '] = df["Salary"] *1.08
print(df)
