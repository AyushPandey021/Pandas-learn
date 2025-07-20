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
    "Age": [
        23,
        25,
        30,
        40,
        41,
        45,
        23,
        22,
        28,
        26,
    ],
    "Salary": [50000, 40000, 40000, 35000, 40000, 23000, 54000, 34000, 32000, 21000],
    "Performance Score": [
        85,
        90,
        32,
        45,
        75,
        76,
        87,
        78,
        97,
        56,
    ],
}
df = pd.DataFrame(data)
print("sample Dataframe⏭️")
print(df)
print("Names (single column  return series )")
name = df['Name']
print(df["Name"]) #select the single coloum


#selecting
subset = df[["Name","Salary"]] #select the 2 coloum

print('\nSubset With Name and Age ')
print(subset)