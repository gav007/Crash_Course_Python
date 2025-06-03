# Create a dictionary with 20 names and their favorite programming languages
fav_progs = {
    "Rachel": "Lua",
    "Bob": "JavaScript",
    "Tina": "MATLAB",
    "Alice": "Python",
    "Quinn": "Elixir",
    "Charlie": "Java",
    "Eve": "Ruby",
    "Peter": "Dart",
    "Frank": "Go",
    "Karen": "Rust",
    "Grace": "Python",
    "Henry": "JavaScript",
    "Ivy": "C#",
    "Jack": "PHP",
    "Liam": "Python",
    "Mia": "Scala",
    "Noah": "Java",
    "Olivia": "Haskell",
    "Sam": "JavaScript",
    "Diana": "C++"
}

# uses sorted function to print the keys in alpha order
for name in sorted(fav_progs.keys()):
    print(f"{name.title()}, Thanks for taking the Poll")

# Print all values in the dictionary
for value in fav_progs.values():
    print(f"This is the value in the dictionary: {value}")

# Count occurrences of each programming language
print("A list of Programming Languages Mentioned in the poll: ")
for value in set(fav_progs.values()):
    print(value)