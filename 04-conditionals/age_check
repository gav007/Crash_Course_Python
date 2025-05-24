# Start program
# Ask the user to enter their age
while True:
    user_age = input("What is your age: ")
    # Read age and convert to integer
    try:
        user_age = int(user_age)
        print(f"Thank you for your age, you are {user_age} years old.")
        break
    except ValueError:
        print("Please enter a valid age: ")
    # Ask the user if they have a student ID (yes/no)
student_id = input("Do you have a student ID? (Yes/No): ")
if student_id.lower() == "yes": 
    student_id = True
elif student_id.lower() == "no":
    student_id = False
else:
    print("Please enter a valid response")
# Read the answer as a string
# If age is less than 18 OR the answer is "yes"
if user_age < 18 or student_id == True:
    print("Discount Granted!")
    # Print "Discount granted"
# Otherwise
else:
    print("No discount for you! ")
    # Print "No discount"
# End program
