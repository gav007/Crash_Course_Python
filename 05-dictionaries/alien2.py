alien_0 = {'color': 'green', 'speed': 'slow', "points": 2}


if "points" in alien_0:
    print("Points are here")
else:
    print("No points")

alien_0 = {'color': 'green', 'speed': 'slow'}

points = alien_0.get("points", "points not found")

print(points)

