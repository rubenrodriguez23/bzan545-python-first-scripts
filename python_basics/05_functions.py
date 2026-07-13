# # Functions
#
# A function is a named chunk of code.
# Use functions when a step has a clear name and you may want to repeat it.
#
# Today-ish:
# * def
# * function body / indentation
# * parameters
# * arguments
# * return
# * print vs return
# * functions calling functions

# def starts a function definition.
# The indented lines are the function body.
def say_howdy():
    print("Howdy")


say_howdy()

# Parameters are input names in the function definition.
# Arguments are actual values passed into the function call.

# Type a greet(name) function:


# Call greet with a few names:


# return sends a value back out of the function.
# Type a calculate_order_total(quantity, unit_price) function:


# Call the function and save the result:


# print vs return:
# * print shows something to a human
# * return gives a value back to the rest of your code

# Type an is_large_order(order_total) function.
# It should return True when order_total is at least 100.


# Functions can call other functions.
# Type a summarize_order(product, quantity, unit_price) function.
# Inside it:
# * calculate the order total
# * check whether it is a large order
# * print a few useful details
# * return the total


# Practice prompts
#
# 1. Write a function that converts dollars to cents.
#
# 2. Write a function that checks whether a state is "TN".
#
# 3. Write a function that builds a shipping message:
#    "shipping from knx to atl on 2026-07-14"
#
# 4. Write a function that takes product, quantity, and unit_price and returns
#    a dictionary with product, quantity, unit_price, and order_total.
#
# 5. Write a function that classifies an order total as "small", "medium", or "large".
#
# 6. Write a function that checks whether a file path ends with ".csv".
