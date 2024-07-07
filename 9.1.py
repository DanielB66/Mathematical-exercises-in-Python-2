import random
import math
hello = "Let's print"
print()
print(hello)
print()
x = random.randint(1, 100)
y = random.randint(1, 100)
print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}".format('x', 'y', 'add', 'subt', 'mult', 'div', 'sqrt'))
print("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10.2f}{:<10.2f}".format(x, y, x+y, x-y, x*y, x/y, math.sqrt(x*x+y*y)))
