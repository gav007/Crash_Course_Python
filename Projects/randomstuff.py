import random

my_list = []


#print(mynum)
while True:
    mynum = random.randint(1,10)
    add_num =input("Add a number to the list? (y/n): ").lower()
    
    if add_num == "y":
        my_list.append(mynum)
        len_list = len(my_list)
        list_summed = sum(my_list)
        print("A new number has been added to the list.")
        print(f"List Length | {len_list}")
        print(f"The Sum of the list is | {list_summed}")
    else:
        if len(my_list) == 0:
            print("No numbers in the list, ya chancer!")
        else:
            counter = 0
            for ele in my_list:
                counter += ele
            print(f"Average | {round(counter/len_list,2)}")
            break
        

