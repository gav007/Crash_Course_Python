responses = []

while True:
    name = input("\nWhats your name chief: ")
    response = input("\nWhats your response: ")
    responses.append((name, response))
    go_again = input("\nWould you like another turn, (y/n): ")
    
    if go_again.lower() != "y":
        break

for name, response in responses:
    print(f"Name: {name}\nResponse: {response}")