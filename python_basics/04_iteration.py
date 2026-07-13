# # Iteration
#
# Iteration means doing something repeatedly.
#
# Today-ish:
# * for loops
# * iterables
# * range()
# * enumerate()
# * zip()
# * accumulators and +=
# * append()
# * while loops
# * break

# A for loop loops over an iterable.
# Iterable is a fancy word for a thing Python can step through.
products = ["hoodie", "cap", "mug", "sticker"]

# Loop through products and print each product:


# Loop through products and print each product in uppercase:


# enumerate() gives both position and value.
# Type a loop that prints the index and product.


# range() is useful when you want a sequence of numbers.
# Type a loop that prints 0, 1, 2, 3.


# Type a loop that prints even numbers from 2 through 10.


# zip() lets you walk through multiple iterables at once.
quantities = [2, 1, 4, 3]
prices = [48.00, 24.00, 16.00, 6.00]

# Loop through quantities and prices together.
# Print each line total.


# Use += to add onto a running total.
total = 0

# Loop through quantities and prices again.
# Add each line total to total.


print(total)

# append() adds one item to the end of a list.
names = ["Arya", "Cersei", "Daenerys", "Hodor", "Ramsay", "Samwell", "Tyrion"]
a_names = []
no_a_names = []

# Loop through names.
# If a name has "a" in it, append to a_names.
# Otherwise append to no_a_names.


print(a_names)
print(no_a_names)

# while loops run until their condition becomes False.
# They are useful, but easier to accidentally make infinite.
countdown = 3

# Type a countdown while loop:


# break exits a loop early.
# while True is an intentional infinite loop, so use break carefully.

# Type a while True loop that prints once and then breaks:


# If a loop goes forever, Ctrl+C in a terminal usually stops it.

# Practice prompts
#
# 1. Loop through products and print a sentence like:
#    "Now checking hoodie"
#
# 2. Calculate the average of the prices list with a loop.
#
# 3. Given order_totals = [48, 144, 16, 288, 72], count how many are at least 100.
#
# 4. Given route_codes = ["knx-atl", "knx-bna", "cha-atl"], build a list of routes
#    that start in Knoxville.
#
# 5. Given product_names = ["Rocky Top Mug", "Checkerboard Cap"], build a list of
#    lowercase URL-ish slugs like "rocky-top-mug".
#
# 6. Use zip() with products, quantities, and prices to print:
#    "2 hoodie orders cost 96.0"
