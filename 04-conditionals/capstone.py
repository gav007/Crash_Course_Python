# Initialize total_points to 0
total_points = 0
colors_list = ["green", "yellow", "red"]
# Start loop to repeat rounds until user wants to quit
    # Prompt user: "Enter the alien color you defeated (green, yellow, red): "
    # Read user input and convert to lowercase
while True:
    user_prompt = input("Enter the alien color you defeated (green, yellow, red): ")
    user_prompt = user_prompt.lower()
    # Validate input: if input not in valid colors list
        # Print "Invalid color, please try again."
        # Continue loop to ask again
    if user_prompt not in colors_list:
        print("Please enter a valid color: ")
    else:
        print(f"You choice was {user_prompt}: ")
        break
        
while True:
    # Use if-elif-else:
        # If alien color is 'green'
            # Add 5 points to total_points
            # Print "You earned 5 points!"
    if user_prompt == "green":
        total_points += 5
        print(f"You earned 5 point and your total is {total_points}")
        # Else if alien color is 'yellow'
            # Add 10 points to total_points
            # Print "You earned 10 points!"
    elif user_prompt == "yellow":
        total_points += 10
        print(f"You earned 10 point and your total is {total_points}")
        # Else (alien color is 'red')
            # Add 15 points to total_points
            # Print "You earned 15 points!"
    else:
        total_points += 15
        print(f"You earned 15 point and your total is {total_points}")

    # Ask user if they want to play again (yes/no)
    # If user says 'no' (case insensitive)
        # Break out of the loop
    play_again = input("Do you wish to play again? (Yes/No)")

    if play_again.lower() == "no":
        print(f"Game Over, your total score was {total_points}")
        break
    else: 
        user_prompt = input("Enter the alien color you defeated (green, yellow, red): ")
    # After loop ends, print "Game Over. You earned a total of <total_points> points."
