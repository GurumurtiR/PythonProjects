# To find a factorial of number

def fact(n):
    if n < 0:
        print('input the positive number')
    elif n == 0:
        print(f'factorial of {n} is{1}')
    else:
        fact = 1
        for i in range(1, n + 1):
           fact *= i
    print(f'factorial of {n}! is: {fact}')
fact(5)