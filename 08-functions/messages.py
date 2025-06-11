# Define a function called show_messages() that prints each text message.
def show_messages(messages):
    for message in messages:
        print(f"MESSAGE: {message}")

# Define a function called send_messages() that moves messages to sent_messages.
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

# Create a list of short text messages.
messages = [
    "Hello!",
    "How are you?",
    "Good morning!",
    "See you soon!",
    "Take care!",
    "Happy birthday!",
    "Congratulations!",
    "Thank you!",
    "Good luck!",
    "Have a great day!"
]

# Call show_messages() to print each message.
show_messages(messages)

# Create a copy of the messages list and a new list for sent messages.
messages_copy = messages[:]
sent_messages = []

# Call send_messages() with the copied list.
send_messages(messages_copy, sent_messages)

# Print both lists to verify the messages were moved correctly.
print("\nOriginal messages:", messages)
print("Sent messages:", sent_messages)