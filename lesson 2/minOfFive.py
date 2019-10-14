num1 = int(input('Enter first number>'))
num2 = int(input('Enter second number>'))
num3 = int(input('Enter third number>'))
num4 = int(input('Enter fourth number>'))
num5 = int(input('Enter fifth number>'))

min = num1
if num2 < min:
    min = num2
if num3 < min:
    min = num3
if num4 < min:
    min = num4
if num5 < min:
    min = num5

print(min)