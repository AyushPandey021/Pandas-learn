import pandas as pd
data ={
  "Time":[1,2,3,4,5,6],

  "Value":[10,None,35,53,None,45,87]

}
df = pd.DataFrame(data)
print("Before interpualation")
print(df)
df['Value'] = df["Value"].interpolate(mathod="linear")
print("After interpulation ")
print(df)
# interpolate the work flow is looking the data and smilear  to add  top and bottom releted valu
# ⏭️inpulation use only this terms [time series data, numeric data ,aviod dropping rows ]
# its use like only numeric data 
