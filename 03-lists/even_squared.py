even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for num in even_numbers:
    print(f"This number {num} squared = {num**2}")


even_numbers2 = list(range(2, 22, 2))

print(even_numbers2[:3])
print(even_numbers2[5:-4])
print(even_numbers2[1:4])
print(even_numbers2[::-1])