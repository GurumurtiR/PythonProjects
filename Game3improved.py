command = ""
started = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("car started.....")
    elif command == "stop":
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped.....")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - To quit
        """)
    elif command == "quit":
         print("sorry, I don't understand that")
         break
