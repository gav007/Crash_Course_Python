import random

print("Welcome to GavBot’s Mad-But-Manageable Python Challenge: The Guessing Game… with a Twist!")
print("The computer has picked a number between 1 and 100. You have 7 shots to guess it!")

secret_number = random.randint(1, 100)
start_attempts = 0
max_attempts = 7

while start_attempts != max_attempts:
    try:
        users_guess = int(input("Whats your guess?: "))
        if users_guess > secret_number:
            print("Too High Ya Sausage!")
            start_attempts += 1
            print(f"Attempts left | {max_attempts - start_attempts}")
        elif users_guess < secret_number:
            print("Too Low Ya Sausage!")
            start_attempts += 1
            print(f"Attempts left | {max_attempts - start_attempts}")
        elif users_guess == secret_number:
            print(f"NICE ONE! your guess {secret_number} was bang on")
            break
    except ValueError:
        print("Just a number please")

print(f"Game Over, ya muppet! The answer was {secret_number}.")  

    