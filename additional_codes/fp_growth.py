# FP-Growth Frequent Pattern Mining Example
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import pandas as pd

try:
    n = int(input("Enter number of transactions: "))
except ValueError:
    print("Invalid input for number of transactions.")
    exit(1)

data = []
for i in range(n):
    line = input("Enter items: ")
    data.append(line.split())

try:
    s = float(input("Enter minimum support: "))
except ValueError:
    print("Invalid input for minimum support.")
    exit(1)

te = TransactionEncoder()
X = te.fit(data).transform(data)
df = pd.DataFrame(X, columns=te.columns_)

freq = fpgrowth(df, min_support=s, use_colnames=True)
print("\nFrequent itemsets:\n")
print(freq)

rules = association_rules(freq, metric='confidence', min_threshold=0.5)
print("\nAssociation Rules:\n")
print(rules[["antecedents", "consequents", "support", "confidence"]])
