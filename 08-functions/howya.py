def howya(name):
    print (f"Howya {name}")

howya("gav")
howya("Sean")

def tea(cuppa="barrys"):
    print(f"Brewing a cuppa {cuppa}")

tea("lyons")
tea()

def chips(*items):
    print("What ya havin pal")
    print("Customer wants: ")
    for item in items:
        print(item)

chips("sausage", "curry")
chips("garlic Bread", "snack box", "onion rings")


def profile(name, **items):
    profile = {"name": name}
    for item, value in items.items():
        profile [item] = value
    return profile

myName = profile("gav")
print(myName)
myName = profile("gav", age=31, location="dublin")
print(myName)

def magic_box(owner, *things, **secret_stuff):
    secrets = {}
    print(f"The owner of this box is {owner}")
    print("="*30)
    print("The items in the box are as follows: ")
    for index, thing in enumerate(things, start=1):
        print(f"{index}: {thing}")
    for item, value in secret_stuff.items():
        secrets[item] = value
    for key, value in secrets.items():
        print(f"{key}: {value}")
    

magic_box("gav","usb", "happy meal", code=1234, location="dublin")