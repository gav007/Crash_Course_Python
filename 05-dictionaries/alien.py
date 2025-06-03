alien_0 = {}
alien_0["x_pos"] = 0
alien_0["y_pos"] = 25
alien_0["speed"] = "medium"

start_position = alien_0["x_pos"]
print(f"Original position: {start_position}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3

alien_0["x_pos"] = start_position + x_increment  

print(f"New Alien Position: {start_position}")
print(alien_0)

#deleting values 
del alien_0["speed"]
print(alien_0)