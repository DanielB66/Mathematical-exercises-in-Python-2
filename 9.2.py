import math
import random
hello = "Let's print"
print(hello)
num_sets = 5  # How many rows?
table_format = "| {:<3} | {:<3} | {:<4} | {:<4} | {:<4} | {:<18} | {:<18} "
print(table_format.format('x', 'y', 'add', 'subt', 'mult', 'div', 'sqrt'))
for _ in range(num_sets):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    add = x + y
    subt = x - y
    mult = x * y
    div = x / y
    sqrt = math.sqrt(x**2 + y**2)
    print(table_format.format(x, y, add, subt, mult, div, sqrt))
