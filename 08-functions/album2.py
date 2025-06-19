def music(artist, album):
    your_artist = {"artist": artist, "album": album}
    return your_artist

get_artist = music("jimi", "eyez")
print(get_artist["artist"])