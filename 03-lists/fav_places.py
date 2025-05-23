# prints a list and then prints it sorted.. 

favorite_places = [
    "Kyoto, Japan",
    "Santorini, Greece",
    "New York City, USA",
    "Paris, France",
    "Swiss Alps, Switzerland",
    "Bora Bora, French Polynesia",
    "Rome, Italy",
    "Great Barrier Reef, Australia",
    "Machu Picchu, Peru",
    "Banff National Park, Canada",
    "Amsterdam, Netherlands",
    "Barcelona, Spain",
    "Prague, Czech Republic",
    "Rio de Janeiro, Brazil",
    "Maui, Hawaii, USA",
    "Queenstown, New Zealand",
    "Reykjavik, Iceland",
    "Venice, Italy",
    "Cape Town, South Africa",
    "Patagonia, Argentina/Chile"
]

for i in favorite_places:
    print(f"I would love to visit {i}")

print("=====================================")

fav_sorted = sorted(favorite_places)

for j in fav_sorted:
    print(f"I would love to visit {j}")


