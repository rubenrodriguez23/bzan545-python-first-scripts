# # Conditionals
#
# Conditionals let Python make decisions.
#
# Today-ish:
# * comparison operators
# * if
# * else
# * elif
# * in and not in
# * is None
# * and / or
# * indentation matters

# Comparison operators:
# * == equal to
# * != not equal to
# * > greater than
# * < less than
# * >= greater than or equal to
# * <= less than or equal to

uf_score = 44
utk_score = 64

# Write an if statement.
# If the Vols won, print "Rocky Top".


# Add an else.
# If the Vols won, print "Vols win".
# Otherwise, print "liar".


# Add an elif.
# If the Vols won by more than the spread, print "Vols won and covered".
# Else if the Vols won, print "Vols won, but did not cover".
# Otherwise, print "Vols did not win".
pre_game_spread = 3.5
margin = utk_score - uf_score


# Tiny comparison example:
x = 10

# Type an if / elif / else block that says whether x is over, under, or equal to 10.


# Beware floating point equality checks.
# This is not Python being silly; this is how decimal values are stored on computers.
# See https://0.30000000000000004.com/
a = 0.3
b = 0.1 + 0.2

print(a == b)
print(a)
print(b)
print(round(a, 8) == round(b, 8))

# in checks whether a value appears inside something else.
# not in checks whether it does not.
category = "apparel"
priority_categories = ["gear", "apparel"]

# Check whether category is in priority_categories:


# Check whether category is not in ["home", "accessories"]:


# None is Python's null-ish value.
tracking_number = None

# Check whether tracking_number is None:


# and / or combine boolean checks.
order_total = 144
quantity = 3
state = "TN"

# Type a check for: order_total is at least 100 AND state is "TN".


# Type a check for: quantity is at least 5 OR order_total is at least 100.


# Indentation matters in Python.
# Lines after a colon belong to the block if they are indented.
#
# In R you may be used to curly braces:
# if (x > 0) {
#   print("positive")
# }
#
# In Python, the indented lines are the block:
# if x > 0:
#     print("positive")

# Practice prompts
#
# 1. Change the scores and rerun the Vols example.
#
# 2. Add an elif for a tied game.
#
# 3. Write an if statement checking whether quantity is at least 5.
#
# 4. An order gets free shipping if order_total is at least 75.
#    Print whether the order gets free shipping.
#
# 5. Inventory should be reordered if stock_on_hand is below reorder_point.
#    Create both variables and print a reorder message when needed.
#
# 6. A route code starts with "knx" for Knoxville.
#    Use string methods and an if statement to check whether a route starts in Knoxville.
#
# 7. A shipment is late if days_in_transit is greater than promised_days.
#    Print "late", "on time", or "early".
