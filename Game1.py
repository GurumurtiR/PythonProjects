command = ""
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "start":
        print("car started.....Ready to go")
    elif command.lower() == "stop":
        print("car stopped")
        break
# instead of using lower() repeatedly