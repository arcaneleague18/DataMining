from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

n = int(input("Enter number of transactions: "))
data = []

for i in range(n):
    data.append(input("Enter itemsets: ").split())

s = float(input("Enter minimum support: "))

te = TransactionEncoder()
X = te.fit(data).transform(data)

df = pd.DataFrame(X, columns=te.columns_)

freq = apriori(df, min_support=s, use_colnames=True)
print("\nFrequent itemsets: ")
print(freq)

rules = association_rules(freq, metric='confidence', min_threshold=0.5)
print("\nAssociation rules: ")
print(rules[["antecedents", "consequents", "support", "confidence"]])