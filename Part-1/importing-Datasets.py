import pandas as pd

#  Read data from CSV file into a datadframe
# CSV is = Comma Separated Values
# importing CSV file⏭️ 
# df = pd.read_csv("sales_data.csv", encoding="latin1")
# df = pd.read_csv(r"C:\Users\vloga\OneDrive\Desktop\Numpy\Pandas\sales_data.csv", encoding="latin1")
# importing Excel file ⏭️
# df = pd.read_excel("Pandas/sales_data.xlsx")
# importing the json file⏭️ 

df = pd.read_json("Pandas/sales_data.json")


print(df)
