# Distance Converter

distance = int(input("input the distance travelled:"))
unit = input("input type k for kms or m for miles:")
if unit.upper() == "K":
    converted = distance/1.609
    print(f"you have covered{converted} miles")
elif unit.upper() == "M":
    converted = distance * 1.609
    print(f"you have covered{converted} kms")
else:
    print("wrong input")