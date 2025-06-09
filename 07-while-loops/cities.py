def ask_for_cities():
    while True:
        city = input(
            "\nPlease enter the name of a city you have visited:\n"
            "(Enter 'quit' when you are finished): "
        )
        if city.lower() == 'quit':
            break
        print(f"I'd love to go to {city.title()}!")

ask_for_cities()
