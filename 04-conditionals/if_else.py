# Start program
# Ask the user to enter a number
user_num = input("Enter a number: ")
try:
    user_num = int(user_num)
except ValueError:
    print("please enter a valid number: ")
    exit()
# If the number is greater than 0
if user_num > 0:
    print("Thats a positive number! ")
    # Print "That's a positive number!"
# Otherwise
else:
    print("Thats a zero or nagative number! ")
    # Print "That's zero or negative"
# End program
