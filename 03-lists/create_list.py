# creates a simple list and prints out the results

my_list = ["milk", "Bread", {"phone_num": "085273****"}, 64]

print(my_list)

my_list.append("snack box")

print(my_list)

my_list.insert(1, "gingernuts")

print(my_list)

del my_list[0]

print(my_list)

item = my_list.pop(2)

print(f"here is the popped item {item}")

for i in my_list:
    print(f"here is the items in my list {i}")

    



