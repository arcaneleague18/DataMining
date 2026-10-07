#data cleaning
import math
data = [10,None, 15, 20, None, 12]

# removing NULL values
cleaned_data = []

for num in data:
    if num is not None:
        cleaned_data.append(num)

print("data after removing NULL values: ", cleaned_data)

# Data Transformation - Normalization


dataset = [10,20,30,40,50]

max_val = max(dataset)
min_val = min(dataset)

normalized_data = []

for num in dataset:
    normalized_value = (num - min_val) / (max_val - min_val)
    normalized_data.append(normalized_value)


print("Normalized data: ", normalized_data)


# Data Integration

dataset1 = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

dataset2 = {
    "name": ["Alice", "Bob", "Charlie"],
    "marks": [85, 90, 95]
}


integrated_data = {}

for key in dataset1:
    integrated_data[key] = dataset1[key]

for key in dataset2:
    if key not in integrated_data:
        integrated_data[key] = dataset2[key]


print("Integrated data: ", integrated_data)