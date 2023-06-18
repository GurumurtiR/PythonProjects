# remove duplicates
number = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for num in number:
    if num not in uniques:
        uniques.append(num)
print(uniques)
