import pandas as pd
import numpy as np 
#  Read data from CSV file into a datadframe
# CSV is = Comma Separated Values
# importing CSV file⏭️
df = pd.read_csv("Pandas/Part-1/Whatsapp_chat.csv", encoding="latin1")

# df = pd.read_csv(r"C:\Users\vloga\OneDrive\Desktop\Numpy\Pandas\sales_data.csv", encoding="latin1")
# importing Excel file ⏭️
# df = pd.read_excel("Pandas/sales_data.xlsx")
# importing the json file⏭️
df_cleaned = df.drop('Unnamed: 0', axis=1)

print(df_cleaned)












