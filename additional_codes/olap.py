# OLAP Operations Example
try:
    n = int(input("Enter records: "))
except ValueError:
    print("Invalid input for number of records.")
    exit(1)

data = []
for i in range(n):
    try:
        product, city, year, sales = input("Product City Year Sales: ").split()
        year = int(year)
        sales = int(sales)
        data.append([product, city, year, sales])
    except Exception as e:
        print("Invalid input for record.", e)
        exit(1)

print("\nData Cube:")
for x in data:
    print(x)

print("\nRoll-up:")
total = sum(x[3] for x in data)
print("Total Sales:", total)

city = input("\nEnter city for Slice: ")
print("Slice:", [x for x in data if x[1] == city])

product = input("\nEnter product for Dice: ")
try:
    year = int(input("Enter year for Dice: "))
except ValueError:
    print("Invalid input for year.")
    exit(1)
print("Dice:", [x for x in data if x[0] == product and x[2] == year])

print("\nDrill-down:")
for x in data:
    print(x)
