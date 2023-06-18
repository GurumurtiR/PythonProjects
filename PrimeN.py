# check prime number

def check(numbers):
    primeNumber = []
    for number in numbers:
        if number > 1:
            for i in range(2, int(number/2) + 1):
                if(number % i) == 0:
                    print(number, 'is not a prime number')
                    break
                else:
                    print(number, 'is a prime number')
            primeNumber.append(number)
        else:
            pass
    return primeNumber
check([2, 3, 4, 5, 6, 7, 8, 9])