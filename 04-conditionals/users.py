# 1. Create a list called current_users with at least 5 usernames.
#    Hint: Just use a simple list with names as strings.

current_users = ["Alice", "Bob", "Charlie", "Dana", "Eve"]

# 2. Create a list called new_users with 5 usernames.
#    Hint: Make sure 1 or 2 are also in current_users, but change their case (e.g., "EVE" and "alice").

new_users = ["alice", "Frank", "EVE", "George", "Hannah"]

# 3. Make a new list lower_current_users, with all usernames from current_users converted to lowercase.
#    Hint: Use a list comprehension with .lower() to convert each username.

lower_current_users = [user.lower() for user in current_users]
print(lower_current_users)

# 4. Loop through each username in new_users:
#    Hint: Use a for loop.
for new_user in new_users:
    new_user.lower()
    if new_user in lower_current_users:
        print("y")
    else:
        print("n")
    # 4a. Convert the username from new_users to lowercase.
    #     Hint: Use .lower() on the username.

    # 4b. Check if the lowercase username is already in lower_current_users.
    #     Hint: Use 'if' and the 'in' keyword.

        # 4b1. If the username is taken, print a message saying it is taken and ask for a new username.
        #      Hint: Use an f-string for formatting if you want.
        #      Example: print(f"Sorry, {username} is already taken. Please enter a new username.")

        # 4b2. Else, print a message saying the username is available.
        #      Example: print(f"{username} is available!")
