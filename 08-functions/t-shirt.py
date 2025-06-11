# Define a function called make_shirt() that accepts a size and a message.
# Modify the make_shirt() function so that shirts are large by default with a default message.
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and the message printed on it is: '{message}'")

# # Call the function using positional arguments.
# make_shirt("Medium", "Python is awesome!")

# # Call the function using keyword arguments.
# make_shirt(size="Large", message="Code like a pro!")

# # Make a large shirt with the default message.
# make_shirt()

# # Make a medium shirt with the default message.
make_shirt(size="Medium", message="Gav is Awesome")

# # Make a shirt of any size with a different message.
# make_shirt(size="Small", message="Keep calm and code on!")