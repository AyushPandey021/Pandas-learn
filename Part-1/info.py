# info()
# for information of data how many 
# entries data and coloum, data usage etc
import pandas as pd

# Use correct path to the file
df = pd.read_csv("C:/Users/vloga/OneDrive/Desktop/Numpy/Pandas/sales_data.csv", encoding="latin1")

print("Displaying the info of data set")
print(df.info())

# df.head(2)
print(df)



