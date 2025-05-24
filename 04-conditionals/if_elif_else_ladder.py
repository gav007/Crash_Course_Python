# Start program
# Ask the user to enter temperature in Celsius
temp = input("Whats the current temperature: ")
# Read the temperature and convert it to an integer
try:
    temp = float(temp)
except:
    print("Please enter a valid value")
# If temperature is less than 0
if temp < 0:
    print("It's Freezing")
    # Print "It's freezing!"
# Else if temperature is between 0 and 15 (inclusive)
elif temp >= 0 and temp <= 15:
    print("It's cold")
    # Print "It's cold."
# Else if temperature is between 16 and 25 (inclusive)
elif temp >= 16 and temp <= 25:
    print("It's warm")
    # Print "It's warm."
# Else (temperature greater than 25)
else:
    print("It's Hot!")
    # Print "It's hot!"
# End program
