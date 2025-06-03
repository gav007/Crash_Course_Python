user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# uses the items() method to fetch the key values pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


# uses the key() method to fetch the key
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(name)

if "erin" not in favorite_languages:
    print("Erin, please take the poll")