# Start program
# Ask the user to enter a number
users_number = "-1"
# Read the number and convert it to an integer
if users_number.isdigit():
    users_number = int(users_number)
    if users_number > 0:
        print("Thats a positive Number.")
    else:
        print("thats a negative number")
else:
    print("please enter a valid number")

# If the number is greater than 0
    # Print "That's a positive number!"
# End program

