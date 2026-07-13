# # CSV pipeline start
#
# A pipeline is a repeatable set of steps.
# Today that can be very small: read data, inspect data, summarize data, write output.
#
# Today-ish:
# * imports
# * paths with Path
# * read a CSV
# * inspect rows, columns, and shape
# * group and summarize
# * write an output file
# * use functions as named pipeline steps

from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/orders.csv")
OUTPUT_DIR = Path("output")
OUTPUT_PATH = OUTPUT_DIR / "category_summary.csv"

# Try changing OUTPUT_PATH later.


def load_orders(path):
    orders = pd.read_csv(path)
    return orders


def summarize_orders(orders):
    summary = (
        orders.groupby("category", as_index=False)
        .agg(
            n_orders=("order_id", "count"),
            total_revenue=("order_total", "sum"),
            avg_order_total=("order_total", "mean"),
        )
        .sort_values("total_revenue", ascending=False)
    )

    return summary


orders = load_orders(DATA_PATH)

print("First rows")
print(orders.head())

print("Columns")
print(orders.columns)

print("Shape")
print(orders.shape)

category_summary = summarize_orders(orders)
print(category_summary)

OUTPUT_DIR.mkdir(exist_ok=True)
category_summary.to_csv(OUTPUT_PATH, index=False)
print(f"Wrote {OUTPUT_PATH}")

# Practice prompts
#
# 1. Change summarize_orders so it groups by state instead of category.
#
# 2. Create high_value_orders with only orders where order_total is at least 100.
#
# 3. Write high_value_orders to output/high_value_orders.csv.
#
# 4. Add a check that the orders data has an order_total column before summarizing.
#
# 5. Add today's date to the output filename.
