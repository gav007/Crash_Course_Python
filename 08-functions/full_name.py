def name_format(firstname, lastname, middlename=""):
    if middlename:
        full_name = f"{firstname} {middlename} {lastname}".title()
    else:
        full_name = f"{firstname} {lastname}".title()
    return full_name

short_name = name_format("gavin", "may")
long_name = name_format("gavin", "sean", "may")

print(short_name)
print(long_name)