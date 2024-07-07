import math
print('enter first point')
x1 = int(input('enter x1: '))
y1 = int(input('enter y1: '))
print('enter second point')
x2 = int(input('enter x2: '))
y2 = int(input('enter y2: '))
distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
print('distance between:', "(", x1, ",", y1, ")", "and", "(", x2, ",", y2, ")", "is", round(distance, 2))
