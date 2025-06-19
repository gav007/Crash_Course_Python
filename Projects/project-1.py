# 1. Set up an empty phonebook dictionary
phonebook = {}  # <- Step 1: Create an empty dictionary for storing names and numbers

# 2. Define a function to add a contact
def add_contact(name, number):
    # Step 2: Store the name and number in the phonebook
    # HINT: Use the name as the key, number as the value
    phonebook[name] = number

# 3. Define a function to look up a contact
def lookup_contact(name):
    # Step 3: Check if the name is in the phonebook
    # If yes, print the number; if not, print "Not found"
    if name in phonebook:
        print(phonebook[name])
    else:
        print(f"The user {name} is not in the phonebook")

# 4. Define a function to list all contacts
def list_contacts():
    # Step 4: Print every name and number in the phonebook
    # HINT: Use a loop over the dictionary's items
    for item, value in phonebook.items():
        print(f"Name: {item} | Number: {value}")

# 5. Main loop: ask the user what they want to do
while True:
    print("\nPhonebook App - Choose an action:")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. List all contacts")
    print("4. Quit")
    choice = input("Enter choice (1-4): ")

    # Step 5A: Add a contact
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        # HINT: Call the add_contact function here
        add_contact(name, number)

    # Step 5B: Look up contact
    elif choice == "2":
        name = input("Enter name to look up: ")
        # HINT: Call the lookup_contact function here
        lookup_contact(name)

    # Step 5C: List all contacts
    elif choice == "3":
        # HINT: Call the list_contacts function here
        list_contacts()

    # Step 5D: Quit the program
    elif choice == "4":
        print("Bye, thanks for using the phonebook!")
        break

    else:
        print("Invalid choice, try again.")

# --- End of Mini-App ---
