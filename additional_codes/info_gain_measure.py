import math

n = int(input("Enter number of records: "))
data = []

for i in range(n):
    a, c = input("Enter Attribute Class: ").split()
    data.append([a, c])

def entropy(rows):
    total = len(rows)
    count = {}
    for r in rows:
        count[r[1]] = count.get(r[1], 0) + 1
    return -sum((v/total) * math.log2(v/total) for v in count.values())

e = entropy(data)
values = set(r[0] for r in data)
weighted = 0

for v in values:
    group = [r for r in data if r[0] == v]
    weighted += len(group) / n * entropy(group)

print("Entropy:", round(e, 3))
print("Information Gain:", round(e - weighted, 3))