# step-1 sample data frame
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
print("Descriptive statistics⏭️")
print(df.describe())


# Descriptive work to discribe the all things in data like min- salary , max - salary , low adn high and all the data h and give the full record of data

print(f'Shape:{df.shape}')
# shape use for define the shape of data rows and coloum  , shape for size to define the data set
print(f'Column Names:{df.columns}')
# df.columns for define the columns  and columns names 

