pet1 = {"type": "rabbit",
        "owner": "john",
        "food": "hoppers",}
pet2= {"type": "fish",
        "owner": "mary",
        "food": "pellets",}
pet3 = {"type": "dog",
        "owner": "mark",
        "food": "hills",}
pet4 = {"type": "mouse",
        "owner": "henry",
        "food": "jerrys",}
pet5 = {"type": "cat",
        "owner": "lou",
        "food": "tom's",}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print("=" * 30)
    print(f"Owner: {pet['owner'].title()}")
    print(f"Pet Type: {pet['type'].capitalize()}")
    print(f"Food Given: {pet['food'].title()}")

found = False

for john in pets:
    if john['owner'] == "john":
        print("John is found")
        found = True
        break
    

