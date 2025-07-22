# Advanced pandas
# what is the interpulation
# 1- preserve data integrity
# 2- smooth trends
# 3 avoid data loss

import pandas as pd

data = {
    "Name": [
        "Ram",
        "Boyka",
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
    "Salary": [60000, 85000, 40000, 35000, 40000, 23000, 54000, 74000, 32000, 21000],
    "Performance_Score": [85, 79 , 32, 45, 75, 76, 87, 78, 97, 56],  # fixed here
}

df= pd.DataFrame(data)
# type of interpulation
# linear , polynomal ,time
df.interpolate(mathod="linear",axis=0 , inplace=True)

