favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

print(favorite_languages)

for key, value in favorite_languages.items():
    print(f"\n{key.title()}'s favourite language is,")
    for language in value:
        print(language)