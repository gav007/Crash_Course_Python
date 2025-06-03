employees = ["Admin", "Karl", "Joan", "Mark", "Susanna", "aDmiN"]

if employees:
    for employee in employees:
        if employee.lower() == "admin":
            print(f"Hello there {employee} would you like to see the status report")
        else:
            print(f"Hello {employee}")
else:
    print("Get more employees")