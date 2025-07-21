import pandas as pd

data = {
    "Name": ["Ram", "Sita", "krishna"],
    "age": [10, 20, 30],
    "city": ["Nagput", "hyderabad", "delhi"],
}
df = pd.DataFrame(data)
print(df)


# df.to_csv("output.csv", index=False) #save in CSV file⏭️
# df.to_excel("output.xlsx", index=False) #save in Excel file⏭️

df.to_json("output.json", index=False)  # save in json file
