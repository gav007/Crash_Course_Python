from art import welcome



# 1. Print a welcome message for the player.
#    Add some ASCII art here to set the scene.
print(welcome)

# 2. Ask the player if they want to go 'left' or 'right' at the crossroad.
#    (Remember: use input() and .lower() for case-insensitive answers.)
user_choice = input("Do you want to go 'Left' or 'Right'?: ").lower()

# 3. If the player chooses 'left':
if user_choice == "left":
    # 3a. Print some lake or boat ASCII art.
    print("Lake")

    # 3b. Ask if they want to 'wait' for a boat or 'swim' across.
    user_choice2 = input("Do you want to 'Wait' or 'Swim' to get across?: ").lower()
    # 3c. If the player chooses 'wait':
    if user_choice2 == "wait":
        # 3c1. Print house/door ASCII art.
        print("Door")
        # 3c2. Ask which door they want: 'red', 'yellow', or 'blue'.
        user_choice3 = input("Choose either 'red', 'yellow', or 'blue': ").lower()
        # 3c3. If they choose 'red':
        if user_choice3 == "red":
            print("Fire")
            exit
            # Print fire ASCII art.
            # Print Game Over message (fire).
        # 3c4. Elif they choose 'yellow':
        elif user_choice3 == "yellow":
            print("treasure")
            # Print treasure ASCII art.
            # Print winning message!
        # 3c5. Elif they choose 'blue':
        elif user_choice3 == "blue":
            print("beasts")
            quit()
            # Print beast ASCII art.
            # Print Game Over message (beasts).
        # 3c6. Else (any other input):
        else:
            print("doesn't exist")
            quit()
            # Print message for choosing a non-existent door (Game Over).
    # 3d. Else (if they swim or give any other answer):
    else:
        print("fish")
        quit()

        # Print fish or piranha ASCII art.
        # Print Game Over message (lake).
# 4. Else (if they choose 'right' or anything else at the crossroad):
else:
    print("hole")
    quit()
    # Print hole or falling ASCII art.
    # Print Game Over message (wrong turn).
