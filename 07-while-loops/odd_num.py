user_range = int(input("How far to check: "))
math_list = []
#print(user_range)

numbers_list = list(range(1, user_range + 1))
#print(numbers_list)


for num in numbers_list:
    if num % 2 == 0:
        math_list.append(num)
    else:
        continue

print(math_list )
