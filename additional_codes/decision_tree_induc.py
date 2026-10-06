from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

n = int(input("Enter number of records: "))
X = []
y = []

for i in range(n):
    a, b, c = map(int, input("Enter Feature1 Feature2 Class: ").split())
    X.append([a, b])
    y.append(c)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

plt.figure(figsize=(8, 5))
plot_tree(model, feature_names=["Feature1", "Feature2"], filled=True)
plt.show()

a, b = map(int, input("Enter test values: ").split())
print("Predicted Class:", model.predict([[a, b]])[0])