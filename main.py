from itertools import product

print(list(map(''.join, product('0123456789ABCDEF', repeat=2))))
print(list(map(''.join, product('0123456789ABCDEF', repeat=4))))
