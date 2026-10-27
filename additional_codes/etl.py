# ETL (Extract, Transform, Load) Example
import pandas as pd

# Extract

data = {
  "Year": [2025, 2025, 2026, 2026],
  "Region": ['north', 'south', 'north', 'south'],
  "Product": ['laptop', 'mobile', 'laptop', 'mobile'],
  "Sales": [100, 200, 150, 250]
}

df = pd.DataFrame(data)
print("Extracted Data:")
print(df)

# Transform
print("\nTransformed DataFrame:")
df['Country'] = ['India', "USA", "India", 'USA']
print(df)

# Load
df.to_csv('dataset.csv', index=True)
print("\nData loaded to dataset.csv")
