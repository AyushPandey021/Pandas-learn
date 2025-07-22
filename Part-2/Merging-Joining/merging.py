# marging for marge the data set rows and column
# syntax
# pd.marge(df1, df2, on="Column_Name", ho="type of join")

# Customer  dataframe
import pandas as pd

df_customers = pd.DataFrame(
    {"CustomerID ": [1, 2, 3], "Name": ["Ramesh", "Suresh", "Kalpesh"]}
)
# order dataframe
df_orders = pd.DataFrame({"CustomerID": [1, 2, 4], "OrderAmount": [250, 450, 350]})
# marge
df_marged = pd.merge(df_customers, df_orders, on="CustomerID", how="right")
print("right join ")
print(df_marged)

df_orders = pd.Dataframe
