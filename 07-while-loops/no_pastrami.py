# 1. Add the sandwich 'pastrami' to the sandwich_orders list at least three times.
sandwich_orders = [
    "Turkey Club",
    "BLT",
    "Grilled Cheese",
    "Ham and Cheese",
    "Veggie",
    "Chicken Salad",
    "Egg Salad",
    "Italian Sub",
    "Meatball Sub",
    "Tuna Melt",
    "Pastrami",
    "Pastrami",
    "Pastrami"
]

# 2. Print a message saying the deli has run out of pastrami.
print("The deli has run out of pastrami.")

# 3. Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

print(sandwich_orders)

# 4. Ensure no pastrami sandwiches end up in finished_sandwiches.
