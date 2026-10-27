# Attribute Oriented Induction Example
try:
    n = int(input("Enter number of records: "))
except ValueError:
    print("Invalid input for number of records.")
    exit(1)

data = []
for i in range(n):
    try:
        name, age, city = input("Enter name age city: ").split()
        age = int(age)
    except Exception as e:
        print("Invalid input for record.", e)
        exit(1)
    age_group = "Young" if age < 30 else "Adult"
    region = "South" if city in ["Hyderabad", "Chennai", "Bangalore"] else "North"
    data.append((age_group, region))

print("\nGeneralized Data:")
for x in sorted(set(data)):
    print(list(x), "Count:", data.count(x))
