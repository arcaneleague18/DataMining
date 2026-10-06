from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
import pandas as pd

n = int(input("Enter number of transactions: "))
data = []

for i in range(n):
    data.append(input("Enter items: ").split())

s = float(input("Enter minimum support: "))

te = TransactionEncoder()
X = te.fit(data).transform(data)

df = pd.DataFrame(X, columns = te.columns_)

freq = fpgrowth(df, min_support=s, use_colnames = True)
print("\nFrequent itemsets:\n")
print(freq)

rules = association_rules(freq, metric='confidence', min_threshold=0.5)
print("\nAssociation Rules:\n")
print(rules[["antecedents", "consequents", "support", "confidence"]])