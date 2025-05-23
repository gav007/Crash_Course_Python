is_a_digit = False
user_input = input("Enter you number: ")

while is_a_digit == False:
    if user_input.isdigit():
        user_input = int(user_input)
        is_a_digit = True
    else:
        print("Please enter a valid number")
        user_input = input("Enter you number: ")
        

n = 0
m = 1
fib = n + m

#for i in range(0, n+1):

