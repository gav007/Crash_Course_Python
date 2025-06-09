# 1. Start by creating an empty dictionary to store the poll results.
polled_results = {}

# 2. Use a while loop to continuously poll users until they choose to stop.
while True:
# 3. Inside the loop, ask the user for their name and their dream vacation destination.
    users_name = input("What's your name?: ")
    dream_vacation = input("What would be your dream vacation?: ") 

# 4. Store the user's response in the dictionary, with their name as the key and the destination as the value.
    response = polled_results[users_name] = dream_vacation

# 5. Ask if they want to let another person respond, and break the loop if they say 'no'.
    finish = input("Do you want to let someone else respond? (yes/no): ").lower().strip()
    if finish == "no":
        break
    
# 6. After polling is complete, print the results of the poll in a clear format.
print("\n--- Poll Results ---")
for name, response in polled_results.items():
    print(f"{name} said they would love to go to {response}")