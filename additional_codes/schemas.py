# Data Warehouse Schemas Example
try:
    n = int(input("Enter number of sales: "))
except ValueError:
    print("Invalid input for number of sales.")
    exit(1)

sales = []
for i in range(n):
    try:
        p, c, d, q = input("Enter Product Category Date Quantity: ").split()
        sales.append([p, c, d, int(q)])
    except Exception as e:
        print("Invalid input for sales record.", e)
        exit(1)

print("\nStar Schema:")
print("Fact_Sales:", sales)
print("Dimensions: Product, Category, Date")

print("\nSnowflake Schema:")
product = list(set(x[0] for x in sales))
category = list(set(x[1] for x in sales))
date = list(set(x[2] for x in sales))
print("Product:", product)
print("Category:", category)
print("Date:", date)
print("Fact_Sales:", sales)

print("\nFact Constellation:")
returns = []
try:
    m = int(input("Enter number of returns: "))
except ValueError:
    print("Invalid input for number of returns.")
    exit(1)
for i in range(m):
    try:
        p, d, q = input("Enter Product Date Quantity: ").split()
        returns.append([p, d, int(q)])
    except Exception as e:
        print("Invalid input for returns record.", e)
        exit(1)

print("Fact_Sales:", sales)
print("Fact_Returns:", returns)
print("Shared Dimensions: Product, Date")
