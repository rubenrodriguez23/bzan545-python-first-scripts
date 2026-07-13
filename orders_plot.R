library(ggplot2)

orders <- read.csv("data/orders.csv")

print("First rows")
print(head(orders))

print("Rows and columns")
print(dim(orders))

ggplot(orders, aes(x = quantity, y = order_total, color = category)) +
  geom_point()
