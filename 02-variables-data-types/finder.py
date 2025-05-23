clutter = "I need to find the word 'find' in this text"

print(clutter)

found = clutter.find("'find'")


if found == -1:
    print("This keyword was not located....")
else:
    print(f"The keyword was found at possition - {found}")


