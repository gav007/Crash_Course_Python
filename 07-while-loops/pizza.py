your_order = []

flag = True

menu = ["cheese", "tomatoe", "pineapple"]
for item in menu:
    print(f"Your choice of toppings include {item} ")

while flag == True:
    
    waiter = input("What would you like from the menu? ")
    
    if waiter.lower() == "cheese":
        your_order.append(waiter)
        print("Is that everything? (y/n)")
        response = input("")
        if response.lower() == "y":
            for cus_order in your_order:
                print(f"toppings include: {cus_order}")
            flag = False

    elif waiter.lower() == "tomatoe":
        your_order.append(waiter)
        print("Is that everything? (y/n)")
        response = input("")
        if response.lower() == "y":
            for cus_order in your_order:
                print(f"toppings include: {cus_order}")
            flag = False

    elif waiter.lower() == "pineapple":
        your_order.append(waiter)
        print("Is that everything? (y/n)")
        response = input("")
        if response.lower() == "y":
            for cus_order in your_order:
                print(f"toppings include: {cus_order}")
            flag = False
    else:
        print("Thats not a valid entry ")