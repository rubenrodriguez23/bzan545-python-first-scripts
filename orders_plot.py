import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

orders = pd.read_csv("data/orders.csv")

print("First rows")
print(orders.head())

print("Rows and columns")
print(orders.shape)

sns.scatterplot(x="quantity", y="order_total", hue="category", data=orders)
plt.show()
