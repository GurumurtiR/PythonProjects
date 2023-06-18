command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started.....")
    elif command == "stop":
        print("car stopped.")
    elif command == "help":
        print("""
start - To start the car
stop - To stop the car
quit - T quit
        """)
    elif command == "quit":
        print("sorry, I don't understand that")
