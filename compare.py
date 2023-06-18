#comparison operator
temp =int(input("Temperature is:"))
if temp > 30:
    print("It is hot day")
elif temp > 10 and  temp<= 30:
    print('it is normal day')
elif temp <= 10:
    print("it is cold day")