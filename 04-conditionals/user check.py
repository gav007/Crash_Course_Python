lower_names = []

names = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Karen", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rachel", "Sam", "Tina",
    "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zack", "Amber", "Blake", "Chloe", "David",
    "Ella", "Finn", "Gia", "Holly", "Ian", "Jasmine", "Kyle", "Lily", "Max", "Nora",
    "Owen", "Paige", "Riley", "Sophia", "Thomas", "Ursula", "Violet", "William", "Xena", "Yosef"
]

for i in names:
    lower_names.append(i.lower())

while True:
    your_name = input("Enter you name here to see if your on the list. ")
    your_name = str(your_name)

    try:
        if your_name.lower() not in lower_names:
            print(f"{your_name}, your not in this list ")
        else:
            print(f"{your_name}, you are on this list")
        break
    except ValueError:
        print("please enter a valid name: ")

