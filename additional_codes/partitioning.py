# Partitioning Example
# Horizontal, Vertical, Round Robin, Hash Based Partitioning

data = []

try:
    n = int(input("Enter number of records: "))
except ValueError:
    print("Invalid input for number of records.")
    exit(1)

for i in range(n):
    try:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        city = input("Enter city: ")
        data.append([id, name, age, city])
    except Exception as e:
        print("Invalid input for record.", e)
        exit(1)

try:
    p = int(input("Enter number of partitions: "))
except ValueError:
    print("Invalid input for number of partitions.")
    exit(1)

print("\nHorizontal partitioning: ")
size = (n + p - 1) // p
for i in range(p):
    print("Partition", i+1, data[i*size:(i+1)*size])

print("\nVertical partitioning: ")
part1 = [[r[0], r[1]] for r in data]  # ID, Name
part2 = [[r[0], r[2], r[3]] for r in data]  # ID, Age, City
print(part1)
print(part2)

print("\nRound Robin Partitioning: ")
rr = [[] for _ in range(p)]
for i, row in enumerate(data):
    rr[i % p].append(row)
for i in range(p):
    print("Partition", i+1, rr[i])

print("\nHash Based Partitioning: ")
h = [[] for _ in range(p)]
for row in data:
    h[row[0] % p].append(row)
for i in range(p):
    print("Partition", i+1, h[i])
