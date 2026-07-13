import csv
import random
from datetime import date, timedelta
from pathlib import Path

from faker import Faker

# Optional: this script creates data/orders.csv.
# Faker is a dev dependency in pyproject.toml because this is setup/data-gen code.

fake = Faker()
random.seed(545)
Faker.seed(545)

output_path = Path(__file__).parent / "orders.csv"

products = [
    ("Smoky Mountain Hoodie", "apparel", 48.00),
    ("Checkerboard Cap", "apparel", 24.00),
    ("Rocky Top Mug", "home", 16.00),
    ("Volunteer Sticker Pack", "accessories", 6.00),
    ("Tailgate Cooler", "gear", 72.00),
    ("Orange Dog Bandana", "accessories", 14.00),
    ("Stadium Blanket", "home", 38.00),
    ("Power T Tumbler", "home", 22.00),
]

states = ["TN", "GA", "NC", "SC", "KY", "AL", "VA", "FL"]
start_date = date(2026, 7, 1)

rows = []
for order_num in range(1, 151):
    product, category, unit_price = random.choice(products)
    quantity = random.randint(1, 6)
    order_date = start_date + timedelta(days=random.randint(0, 20))
    order_total = round(quantity * unit_price, 2)

    rows.append(
        {
            "order_id": 1000 + order_num,
            "order_date": order_date.isoformat(),
            "customer_name": fake.name(),
            "state": random.choice(states),
            "product": product,
            "category": category,
            "quantity": quantity,
            "unit_price": unit_price,
            "order_total": order_total,
        }
    )

with output_path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {output_path}")
