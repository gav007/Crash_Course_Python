# starts an empty list
aliens = []

# make 30 aliens
for alien_number in range(0, 30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# changes the value of the first 3 objects in the list
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# show the first 5 aliens from the list aliens
for alien in aliens[0:5]:
    print(alien)
print(".....")

print(f"Total number of aliens: {len(aliens)}")
