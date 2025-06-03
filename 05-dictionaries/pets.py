# Create dictionaries for each pet
pet1 = {"type": "dog", "owner": "Alice"}
pet2 = {"type": "cat", "owner": "Bob"}
pet3 = {"type": "parrot", "owner": "Charlie"}
pet4 = {"type": "rabbit", "owner": "Diana"}
pet5 = {"type": "hamster", "owner": "Eve"}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4, pet5]

# Loop through the list and print everything about each pet
for pet in pets:
    print("\nPet details:")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")