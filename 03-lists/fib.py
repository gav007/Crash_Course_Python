# Ask the user for how many Fibonacci numbers they want
n = int(input("How many Fibonacci numbers would you like to generate? "))

# Handle small inputs
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    fib_sequence = [0]
else:
    # Start with the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci numbers from 2 up to n-1
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)

# Print the resulting Fibonacci sequence
print(f"First {n} Fibonacci numbers:")
print(fib_sequence)
