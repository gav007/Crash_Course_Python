your_order = []
menu = ["cheese", "tomato", "pineapple"]

# Show the menu once
print("Right here’s the f**kin menu chief:")
for item in menu:
    print(f"- {item}")

while True:
    waiter = input("What d’ya want on yer pizza? ").lower()

    if waiter in menu:
        your_order.append(waiter)
        response = input("That it? (y/n) ").lower()
        if response == "y":
            print("\nSound, yer pizza’s gettin’ topped with:")
            for cus_order in your_order:
                print(f"🍕 {cus_order}")
            break
    else:
        print("That’s not on the menu, pal. Pick from what’s there.")
