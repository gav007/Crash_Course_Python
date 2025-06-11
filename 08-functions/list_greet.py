names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Frank",
    "Grace",
    "Hannah",
    "Ivy",
    "Jack"
]

def greet(names_list):
    for ele in names_list:
        print(f"Charmed to meet you {ele.title().strip("")}")

greet(names)