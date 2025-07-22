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

df.dropna(inplace=True)
print(df)