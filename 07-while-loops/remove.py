pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

cat_list = []

while "cat" in pets:
    cat_list.append("cat")
    pets.remove("cat")  # Removes "cat" from the pets list

print(cat_list)  # List of removed "cat" entries
print(pets)      # Updated pets list without "cat"