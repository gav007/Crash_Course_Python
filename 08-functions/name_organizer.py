names = [
    "charlie",
    "alice",
    "jack",
    "grace",
    "david",
    "hannah",
    "eve",
    "bob",
    "ivy",
    "frank"
]

def name_title(untitled_list):
    titled_names = []
    for name in untitled_list:
        cap_names = name.title()
        titled_names.append(cap_names)
    return titled_names

def name_sorted(unsorted_list):
    sorted_list = sorted(unsorted_list)
    return sorted_list

test1 = name_title(names)
print(test1)

test2 = name_sorted(test1)
for name in test2:
    print(f"Name = {name}")
print(test2)