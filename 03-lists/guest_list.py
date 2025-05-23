

guests = [
    "Alice Smith", "Bob Johnson", "Charlie Brown", "Diana Miller", "Eve Davis",
    "Frank White", "Grace Taylor", "Henry Wilson", "Ivy Moore", "Jack Green",
    "Karen Hall", "Liam King", "Mia Wright", "Noah Scott", "Olivia Adams",
    "Peter Baker", "Quinn Parker", "Rachel Hill", "Sam Turner", "Tina Campbell"
]

target_name = "liam king"

lower_case_list = []

for guest in guests:
    lower_case_list.append(guest.lower())

if target_name in lower_case_list:
    index = lower_case_list.index(target_name)

    remove_guest = guests.pop(index)

    print(f"{remove_guest} was found at position {index + 1} in the line\nHe has now been removed from the party")

else: 
    print(f"{target_name} was not in the line")

for guest in guests:
    print(f"> welcome to the party {guest}")




    

