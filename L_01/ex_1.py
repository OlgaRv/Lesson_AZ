import pandas as pd

data = [1, 2, 3, 4, 5]
serias = pd.Series(data)

print(serias)


data = {
    "Name": ["John", "Jane", "Mary"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
}

df1 = pd.DataFrame(data)
df1.to_csv('output.csv', index=False)
print(df1.loc[:,['Name', 'Age']])

df2 = pd.read_csv("World-happiness-report-2024.csv")

print(df2)
print(df2.head())
print(df2.tail())
print(df2.info())
print(df2.describe())
print(df2['Country name'])
print(df2[['Country name', 'Regional indicator']])
print(df2.loc[55])
print(df2.loc[55, 'Social support'])
print(df2[df2['Social support'] > 0.9])
print(df2.sample(frac=0.1))