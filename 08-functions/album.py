# Define a function called make_album() that builds a dictionary describing a music album.
def make_album(artist, title, num_songs=None):
    album = {"artist": artist, "title": title}
    if num_songs:
        album["num_songs"] = num_songs
    return album

# Use the function to make three dictionaries representing different albums.
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Ed Sheeran", "Divide")
album3 = make_album("Adele", "25", num_songs=11)

# Print each return value to show that the dictionaries are storing the album information correctly.
print(album1)
print(album2)
print(album3)

# Add a while loop to allow users to enter album details.
while True:
    print("\nEnter album details (or type 'quit' to exit):")
    artist = input("Artist name: ").strip()
    if artist.lower() == 'quit':
        break
    title = input("Album title: ").strip()
    if title.lower() == 'quit':
        break
    num_songs = input("Number of songs (optional, press Enter to skip): ").strip()
    num_songs = int(num_songs) if num_songs.isdigit() else None

    album = make_album(artist, title, num_songs)
    print("Album created:", album)