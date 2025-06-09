prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    cities = input(prompt)

    if cities.lower() == "quit":
        break
    else:
        print(f"I would love to go to {cities}")