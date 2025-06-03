# Start program
# Create at least 10 different tests:

# Test 1: Check if a string equals another string
stringA = "cat"
stringB = "Cat"
print(stringA == stringB)
# Test 2: Check if a string does NOT equal another string
stringA = "cat"
stringB = "Cat"
print(stringA != stringB)
# Test 3: Use .lower() on a string and check equality
stringA = "cat"
stringB = "Cat"
print(stringA.lower() == stringB.lower())
# Test 4: Check if a number is equal to another number
num1 = 4
num2 = 8
print(num1 == num2)
# Test 5: Check if a number is NOT equal to another number
num1 = 4
num2 = 8
print(num1 != num2)
# Test 6: Check if a number is greater than another number
num1 = 4
num2 = 8
print(num1 > num2)
# Test 7: Check if a number is less than or equal to another number
num1 = 4
num2 = 8
print(num1 <= num2)
# Test 8: Use 'and' to combine two conditions
num1 = 4
num2 = 8
print("Test 8: num1 < num2 and num2 > 0")
print("Expected: True")
print(num1 < num2 and num2 > 0)

# Test 9: Use 'or' to combine two conditions
print("Test 9: num1 > num2 or num2 > 0")
print("Expected: True")
print(num1 > num2 or num2 > 0)

# Test 10: Check if an item is in a list
animals = ["cat", "dog", "mouse"]
print("Test 10: 'cat' in animals")
print("Expected: True")
print("cat" in animals)

# Test 11: Check if an item is NOT in a list
print("Test 11: 'elephant' not in animals")
print("Expected: True")
print("elephant" not in animals)
# End program
