def cities(where, location):
    full_place = f"{where}, {location}"
    return full_place.title()

new_place = cities("dublin", "Ireland")

print(new_place)
new_place = cities("milan", "italy")
print(new_place)