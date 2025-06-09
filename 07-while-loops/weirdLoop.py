responses = {}

polling_active = True

while polling_active == True:
    print("============================")
    name = input("\nwhat is your name? ")
    response = input("What is your response? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print("\n===Responses===")
for name, response in responses.items():
    print(f"User: {name}\nResponse{response}")