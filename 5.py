number = int(input('enter a 3-digits integer number: '))
sum = number % 10
number = number // 10
sum += number % 10
number = number // 10
sum += number % 10
print('sum of digits:', sum)
