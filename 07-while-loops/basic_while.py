import time
counter = 1

while counter <= 5:
    print(f"Counter is at {counter}")
    counter += 1
    time.sleep(1)
    if counter == 5:
        print("It's almost time... ")
        time.sleep(2)
        print("Time is up!")
        print("BANG!")
        break