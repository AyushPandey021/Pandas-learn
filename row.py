#head()
# head return top rows
#tail() 
# tails retun bottom rows 
import pandas as pd

# Use correct path to the file
df = pd.read_csv("C:/Users/vloga/OneDrive/Desktop/Numpy/Pandas/sales_data.csv", encoding="latin1")
print('Display the 5 rows in data top🔝')
print(df.head(2))


# df.head(2)
print("Display 5 rows in list in bottom↙️")
print(df.tail(2))



