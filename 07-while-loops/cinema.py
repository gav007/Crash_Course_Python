

while True:

    try:
        users_age = int(input("What's yer age pal: "))

        if users_age == 0  or users_age <= 3:
            print(f"Jammy fecker, you got in for free ")
        elif users_age <= 12:
            print(f"Right pal, thats going to be 10 blips ")
        elif users_age > 12:
            print(f"Max punishment pal, thats 15 yo yo's")
        else:
            print("Quit talking shite will ya ")

    except ValueError:
        print("That's not a bleedin number ya plank ")
        continue
    
    response = input("that all ya want? (y/n) ")

    if response.lower() == "y":
        print("Right so, feck off now ")
        break 