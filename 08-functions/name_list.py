names = []

def formatted_names(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    add_name = input("Do you want to add a name? ").lower()
    if add_name == "y":
        first_name = input("Whats the first name: ")
        last_name = input("Whats the last name: ")
        name_added = formatted_names(first_name, last_name)
        names.append(name_added)
        print("The name has been added to the list")
    else:
        print(names)
        break