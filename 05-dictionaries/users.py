from colorama import Fore, Back, Style

usernames = {
    "rapidman": {
        "first_name": "gav",
        "last_name": "May",
        "location": "spain",
    },

    "roxy": {
        "first_name": "jill",
        "last_name": "banks",
        "location": "france",

    }
}

for user, name in usernames.items():
    print(f"\nThe UserName is: {user}")
    full_name = f"{name['first_name'].title()} {name['last_name'].title()}"
    location = f"{name['location'].title()}"

    print(f"Their full name is {Fore.BLUE + full_name + Style.RESET_ALL}")
    print(f"Their location is {location}")

    