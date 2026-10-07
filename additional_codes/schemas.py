n = int(input("Enter number of sales: "))

sales = []
for i in range(n):
    p, c, d, q = input("Enter Product Category Date Quantity: ").split()
    sales.append([p, c, d, int(q)])

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
m = int(input("Enter number of returns: "))
for i in range(m):
    p, d, q = input("Enter Product Date Quantity: ").split()
    returns.append([p, d, int(q)])

print("Fact_Sales:", sales)
print("Fact_Returns:", returns)
print("Shared Dimensions: Product, Date")