import pandas as pd

data = {
  "Year": [2025, 2025, 2026, 2026],
  "Region": ['north', 'south', 'north', 'south'],
  "Product": ['laptop', 'mobile', 'laptop', 'mobile'],
  "Sales": [100,200,150,250]
}

# extract

df = pd.DataFrame(data)
print(df)

# Transform

print("Tranformed dataframe")
df['Country'] = ['India', "USA", "India", 'USA']

print(df)

#load

df.to_csv('dataset.csv', index=True)