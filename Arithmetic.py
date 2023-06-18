# sample arithmatic operations

a = int(input('enter the value of a:'))
b = int(input('enter the value of b:'))
add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
print('sum: {0}, dif: {1}, mult: {2}, div: {3}, mod: {4}'.format(add, sub, mul, div, mod))
print('sum: %d, dif: %d, mult: %d, div: %2f, mod: %d' % (add, sub, mul, div, mod))

print("{0:<4} | {1:<4} | {2:<4} | {3:>4}".format('sum', 'diff', 'mul', 'div'))
print("{0:<4} | {1:<4} | {2:<4} | {3:>4}".format(add, sub, mul, div))
