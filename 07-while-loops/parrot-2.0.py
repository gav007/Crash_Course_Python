user_message = input("Tell me a message and i'll repeat it to you ")

while user_message:
    print(user_message)
    user_message = input("Tell me a message and i'll repeat it to you ")
    if user_message == "quit":
        print("goodbye")
        break