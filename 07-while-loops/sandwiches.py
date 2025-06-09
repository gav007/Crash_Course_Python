# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.

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
        "Tuna Melt"]

# Then make an empty list called finished_sandwiches.

finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.

print("-" * 10 + "The Waiting Area" + "-" * 10)
for order in sandwich_orders:
        print(f"\n- Your order {order} is being prepared.")
        

while sandwich_orders:
    #print(sandwich_orders)
    finished_sambo = sandwich_orders.pop()
    finished_sandwiches.append(finished_sambo)    

#print(finished_sandwiches)

# After all the sandwiches have been made, print a message listing each sandwich that was made.

print("-" * 10 + "The Deli Counter" + "-" * 10)
for finished_sambos in finished_sandwiches:
    print(f"\n- Your {finished_sambos} was made\n- Thank you for your order")
    print("-" * 36)






