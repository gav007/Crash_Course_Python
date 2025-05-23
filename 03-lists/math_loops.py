# loop to calculate the sum of numbers from 1 - 1000
sum = 0

numbers_list = list(range(1, 1001))


for num in numbers_list:
    sum += num

print(f"The sum of the numbers in the range 1 to 1000 is {sum}")

n = int(input("Enter the number you want to sum up: "))

total = n*(n+1)//2

print(f"The sum of numbers from 1 to {n} is {total}")

