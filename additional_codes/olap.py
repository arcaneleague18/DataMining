n = int(input("Enter records: "))
data = []

for i in range(n):
    product, city, year, sales = input("Product City Year Sales: ").split()
    data.append([product, city, int(year), int(sales)])

print("\nData Cube:")
for x in data:
    print(x)

print("\nRoll-up:")
total = sum(x[3] for x in data)
print("Total Sales:", total)

city = input("\nEnter city for Slice: ")
print("Slice:", [x for x in data if x[1] == city])  

product = input("\nEnter product for Dice: ")
year = int(input("Enter year for Dice: "))
print("Dice:", [x for x in data if x[0] == product and x[2] == year])

print("\nDrill-down:")
for x in data:
    print(x) 