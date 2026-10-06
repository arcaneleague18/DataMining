n = int(input("Enter number of records: "))
data = []

for i in range(n):
    name, age, city = input("Enter name age city: ").split()
    age = int(age)
    age_group = "Young" if age < 30 else "Adult"
    region = "South" if city in ["Hyderabad", "Chennai", "Bangalore"] else "North"

    data.append((age_group, region))

print("\n Generalized Data: ")
for x in sorted(set(data)):
    print(list(x), "Count: ", data.count(x))