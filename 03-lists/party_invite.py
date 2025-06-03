# Party Invitation Manager (Basic) - Pseudocode

# 1. Create and manage guest list with variables and lists
# Initialize a list with some guest names

guest_names = [
                "Alice", "Bob", "Charlie", "Diana", "Eve",
                "Frank", "Grace", "Henry", "Ivy", "Jack"
              ]

# 2. Add guests to the list
# Use list methods like append() or insert() to add new guests

new_guest = "Charlie Brown"
guest_names.append(new_guest)
print(guest_names)

# 3. Remove guests by position or last item (no conditionals yet)
# Use list.pop() or del statement to remove guests

del guest_names[0]
guest_names.remove("Grace")
guest_names.pop(3)
print(guest_names)

# 4. Print personalized invitations using loops and string formatting
# Loop through the guest list
# For each guest, print a personalized invitation message using f-strings

for guest in guest_names:
    print(f">Welcome to the party {guest}")



# 5. Sort and display the guest list alphabetically
# Use sorted() to get a new sorted list without modifying the original
# Print the sorted guest list

sorted_list = sorted(guest_names)
print(sorted_list)

for i, val in enumerate(guest_names):
    print(i +1 , val)