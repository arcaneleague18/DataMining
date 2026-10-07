1.Data Processing Techniques:
import pandas as pd

# Creating sample data
data1 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [20, 25, None, 30, 25],
    'Salary': [30000, 40000, 35000, None, 40000],
    'City': ['Hyderabad', 'Delhi', 'Mumbai', 'Hyderabad', None]
}

df1 = pd.DataFrame(data1)

print("Original Data:")
print(df1)


# ------------------------------------------------
# 1. DATA CLEANING
# ------------------------------------------------

# Remove duplicate rows
df1 = df1.drop_duplicates()

# Fill missing numerical values with mean
df1['Age'] = df1['Age'].fillna(df1['Age'].mean())
df1['Salary'] = df1['Salary'].fillna(df1['Salary'].mean())

# Fill missing categorical values with mode
df1['City'] = df1['City'].fillna(df1['City'].mode()[0])

print("\nAfter Data Cleaning:")
print(df1)


# ------------------------------------------------
# 2. DATA TRANSFORMATION - NORMALIZATION
# ------------------------------------------------

# Min-Max Normalization
df1['Age'] = (df1['Age'] - df1['Age'].min()) / (df1['Age'].max() - df1['Age'].min())

df1['Salary'] = (df1['Salary'] - df1['Salary'].min()) / (df1['Salary'].max() - df1['Salary'].min())

print("\nAfter Normalization:")
print(df1)


# ------------------------------------------------
# 3. DATA INTEGRATION
# ------------------------------------------------

data2 = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['IT', 'HR', 'AI', 'IT', 'Finance']
}

df2 = pd.DataFrame(data2)

# Merge two datasets
integrated_data = pd.merge(df1, df2, on='Name')

print("\nAfter Data Integration:")
print(integrated_data)

2. Partitioning - Horizontal, Vertical, Round Robin, Hash based 

import pandas as pd

# Sample dataset
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
    'Age': [20, 21, 22, 23, 24, 25, 26, 27],
    'Marks': [85, 90, 78, 88, 92, 75, 80, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


# ------------------------------------------------
# 1. HORIZONTAL PARTITIONING
# ------------------------------------------------
# Dividing rows into partitions

horizontal_p1 = df.iloc[:4]
horizontal_p2 = df.iloc[4:]

print("\nHorizontal Partition 1:")
print(horizontal_p1)

print("\nHorizontal Partition 2:")
print(horizontal_p2)


# ------------------------------------------------
# 2. VERTICAL PARTITIONING
# ------------------------------------------------
# Dividing columns into partitions

vertical_p1 = df[['ID', 'Name']]
vertical_p2 = df[['Age', 'Marks']]

print("\nVertical Partition 1:")
print(vertical_p1)

print("\nVertical Partition 2:")
print(vertical_p2)


# ------------------------------------------------
# 3. ROUND ROBIN PARTITIONING
# ------------------------------------------------
# Distribute rows cyclically among partitions

n = 2   # Number of partitions

round_robin_p1 = df.iloc[0::n]
round_robin_p2 = df.iloc[1::n]

print("\nRound Robin Partition 1:")
print(round_robin_p1)

print("\nRound Robin Partition 2:")
print(round_robin_p2)


# ------------------------------------------------
# 4. HASH-BASED PARTITIONING
# ------------------------------------------------
# Partition rows based on hash value of ID

hash_p1 = df[df['ID'] % 2 == 0]
hash_p2 = df[df['ID'] % 2 != 0]

print("\nHash Partition 1 (ID % 2 = 0):")
print(hash_p1)

print("\nHash Partition 2 (ID % 2 != 0):")
print(hash_p2)

3. Data Warehouse schemas – star, snowflake, fact constellation 
import pandas as pd

# 1. STAR SCHEMA
# One Fact table connected to multiple Dimension tables

fact_sales = pd.DataFrame({
    "Product_ID": [1, 2, 3],
    "Customer_ID": [101, 102, 103],
    "Sales": [500, 700, 900]
})

dim_product = pd.DataFrame({
    "Product_ID": [1, 2, 3],
    "Product": ["Laptop", "Phone", "Tablet"]
})

dim_customer = pd.DataFrame({
    "Customer_ID": [101, 102, 103],
    "Customer": ["A", "B", "C"]
})

print("STAR SCHEMA")
print(fact_sales)
print(dim_product)
print(dim_customer)


# 2. SNOWFLAKE SCHEMA
# Dimension tables are further divided into sub-dimensions

dim_product = pd.DataFrame({
    "Product_ID": [1, 2],
    "Product": ["Laptop", "Phone"],
    "Category_ID": [10, 20]
})

dim_category = pd.DataFrame({
    "Category_ID": [10, 20],
    "Category": ["Computer", "Mobile"]
})

print("\nSNOWFLAKE SCHEMA")
print(dim_product)
print(dim_category)
snowflake = pd.merge(dim_product, dim_category, on='Category_ID')
print("\nAfter Joining:")
print(snowflake)

# 3. FACT CONSTELLATION
# Multiple fact tables share common dimension tables

fact_sales = pd.DataFrame({
    "Product_ID": [1, 2],
    "Sales": [500, 700]
})

fact_returns = pd.DataFrame({
    "Product_ID": [1, 2],
    "Returns": [20, 30]
})

dim_product = pd.DataFrame({
    "Product_ID": [1, 2],
    "Product": ["Laptop", "Phone"]
})

print("\nFACT CONSTELLATION")
print(fact_sales)
print(fact_returns)
print(dim_product)

4. OLAP

import pandas as pd

# -----------------------------------------
# DATA CUBE
# -----------------------------------------

data = {
    'Year': [2024, 2024, 2025, 2025],
    'City': ['Hyderabad', 'Delhi', 'Hyderabad', 'Delhi'],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Mobile'],
    'Sales': [50000, 30000, 60000, 40000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# -----------------------------------------
# 1. ROLL-UP
# -----------------------------------------
# Total sales by Year

rollup = df.groupby('Year')['Sales'].sum()

print("\n1. ROLL-UP - Total Sales by Year:")
print(rollup)


# -----------------------------------------
# 2. DRILL-DOWN
# -----------------------------------------
# Sales by Year and City

drilldown = df.groupby(['Year', 'City'])['Sales'].sum()

print("\n2. DRILL-DOWN - Sales by Year and City:")
print(drilldown)


# -----------------------------------------
# 3. SLICE
# -----------------------------------------
# Select one Year

slice_data = df[df['Year'] == 2025]

print("\n3. SLICE - Sales for 2025:")
print(slice_data)


# -----------------------------------------
# 4. DICE
# -----------------------------------------
# Select Hyderabad + Laptop

dice_data = df[
    (df['City'] == 'Hyderabad') &
    (df['Product'] == 'Laptop')
]

print("\n4. DICE - Hyderabad Laptop Sales:")
print(dice_data)


# -----------------------------------------
# 5. PIVOT
# -----------------------------------------
# City vs Year

pivot = pd.pivot_table(
    df,
    values='Sales',
    index='City',
    columns='Year',
    aggfunc='sum'
)

print("\n5. PIVOT - City vs Year:")
print(pivot)

5. Data Extraction, Transformations & Loading operations 
import pandas as pd
# =================================================
# 1. DATA EXTRACTION
# =================================================
# Create sample employee data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, None, 35],
    'Salary': [40000, 50000, 45000, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("employees.csv", index=False)

# Extract data from CSV
data = pd.read_csv("employees.csv")

print("Extracted Data:")
print(data)
# =================================================
# 2. DATA TRANSFORMATION
# =================================================
# Remove duplicate records
data = data.drop_duplicates()

# Handle missing values
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

# Convert Name to uppercase
data['Name'] = data['Name'].str.upper()

# Increase salary by 10%
data['Salary'] = data['Salary'] * 1.10

# Create new column
data['Salary_Lakh'] = data['Salary'] / 100000

print("\nTransformed Data:")
print(data)


# =================================================
# 3. DATA LOADING
# =================================================

# Save transformed data
data.to_csv("employees_transformed.csv", index=False)

print("\nData successfully loaded!")

6. Implementation of Attribute oriented induction algorithm 
import pandas as pd

# -----------------------------------------
# STEP 1: Create the dataset
# -----------------------------------------

data = {
    'Age': [20, 22, 25, 35, 38, 42, 45, 50],
    'City': ['Hyderabad', 'Hyderabad', 'Delhi', 'Delhi',
             'Mumbai', 'Mumbai', 'Chennai', 'Chennai'],
    'Salary': [25000, 30000, 40000, 45000,
               55000, 60000, 70000, 75000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# -----------------------------------------
# STEP 2: Generalize Age
# -----------------------------------------

def age_group(age):
    if age < 30:
        return 'Young'
    elif age < 40:
        return 'Middle'
    else:
        return 'Senior'

df['Age_Group'] = df['Age'].apply(age_group)


# -----------------------------------------
# STEP 3: Generalize City
# -----------------------------------------

def city_group(city):
    if city in ['Hyderabad', 'Delhi']:
        return 'North/South Central'
    else:
        return 'Other Cities'

df['City_Group'] = df['City'].apply(city_group)


# -----------------------------------------
# STEP 4: Generalize Salary
# -----------------------------------------

def salary_group(salary):
    if salary < 40000:
        return 'Low'
    elif salary < 60000:
        return 'Medium'
    else:
        return 'High'

df['Salary_Group'] = df['Salary'].apply(salary_group)


# -----------------------------------------
# STEP 5: Count generalized tuples
# -----------------------------------------

result = df.groupby(
    ['Age_Group', 'City_Group', 'Salary_Group']
).size().reset_index(name='Count')


print("\nGeneralized Data:")
print(result)

7. Implementation of apriori algorithm 
from itertools import combinations

# Small dataset
transactions = [


    ['Milk', 'Bread'],
    ['Milk', 'Bread'],
    ['Milk', 'Egg'],
    ['Bread', 'Egg'],
    ['Milk', 'Bread']
]

min_support = 2


# Find support
def support(itemset):
    count = 0

    for t in transactions:
        if set(itemset).issubset(set(t)):
            count += 1

    return count


# Get all items
items = sorted(set(item for t in transactions for item in t))

# Generate itemsets
for k in range(1, len(items) + 1):

    print("\n", k, "-itemsets:")

    for itemset in combinations(items, k):

        count = support(itemset)

        if count >= min_support:
            print(itemset, "Support =", count/len(transactions))

9. Implementation of Decision Tree Induction 
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Small dataset
data = {
    'Age': [20, 25, 30, 35, 40, 45],
    'Income': [20, 25, 30, 40, 50, 60],
    'Buy': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# Convert target into numbers
df['Buy'] = df['Buy'].map({'No': 0, 'Yes': 1})


# Input and output
X = df[['Age', 'Income']]
y = df['Buy']


# Create Decision Tree
model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=2,
    random_state=1
)

# Train the model
model.fit(X, y)


# Predict
prediction = model.predict(pd.DataFrame([[28, 28]], columns=['Age', 'Income']))

if prediction[0] == 1:
    print("\nPrediction: YES")
else:
    print("\nPrediction: NO")


# Display Decision Tree

plot_tree(
    model,
    feature_names=['Age', 'Income'],
    class_names=['No', 'Yes'],
    filled=True
)

plt.show()

10. Calculating Information gain measures 
import pandas as pd
import math

# Small dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Rainy', 'Rainy', 'Sunny', 'Rainy'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# -----------------------------------------
# Entropy Function
# -----------------------------------------

def entropy(data):
    counts = data.value_counts()
    total = len(data)

    result = 0

    for count in counts:
        p = count / total
        result -= p * math.log2(p)

    return result


# -----------------------------------------
# Calculate Total Entropy
# -----------------------------------------

total_entropy = entropy(df['Play'])

print("\nTotal Entropy:")
print(round(total_entropy, 3))


# -----------------------------------------
# Calculate Weighted Entropy
# -----------------------------------------

weighted_entropy = 0

for value in df['Outlook'].unique():

    subset = df[df['Outlook'] == value]

    e = entropy(subset['Play'])

    weight = len(subset) / len(df)

    weighted_entropy += weight * e

    print("\n", value)
    print("Entropy =", round(e, 3))


# -----------------------------------------
# Information Gain
# -----------------------------------------

information_gain = total_entropy - weighted_entropy

print("\nWeighted Entropy:")
print(round(weighted_entropy, 3))

print("\nInformation Gain:")
print(round(information_gain, 3))
