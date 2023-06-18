# if statemeruents in programming
is_hot = True
is_cold = False
if is_hot and is_cold:
    print("it`s a normal day")
    print("no need to do anything")
elif is_hot:
    temp = str(input("mention the temperature: "))
    if (temp > '25' and temp <= '35 '):
        print("it`s okay normal in india")
    elif (temp > '35'):
        print('it`s very hot day')
        print("drink plenty of water")
elif is_cold:
    print("it`s a cold day")
    print("wear warm cloths")
else:
    print("it`s a lovely day")
print("enjoy your day")