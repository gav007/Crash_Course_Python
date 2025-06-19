def greet(f_name, l_name):
    full_name = f"{f_name} {l_name}"
    return full_name.title()


while True:
    first_name = input("What's your first name?: ")
    last_name = input("What's your last name?: ")
    greeting = greet(first_name, last_name)
    print(f"A pleasure to meet you {greeting}")