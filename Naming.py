name = str(input("Enter the name:"))
if len(name) < 3:
    print("name must be atleast three characters")
elif len(name) > 40:
    print("name is too long it needs to be short and precise manner")
else:
    print("name looks good")