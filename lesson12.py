# Оператор if

# Операторы сравнения
print(2 > 3)  # больше
print(2 >= 3)  # больше либо равно
print(2 < 3)  # меньше
print(2 <= 3)  # меньше либо равно
print(2 != 3)  # неравенство
print(2 == 3)  # равенство
print('h' > 'a')  # True

'''
if выражение 1:
    блок кода 1
elif выражение 2:
    блок кода 2
else:
    блок кода 3
'''

# example false
x = 0
if x:
    print("переменная х истинна")
else:
    print("переменная х ложна")

# example true
if 5:
    print("переменная х истинно")
else:
    print("переменная х ложно")

# example1
light = 'red'
if light == 'red':
    print('STOP')
elif light == 'yellow':
    print('WAIT')
elif light == 'green':
    print('GO')
else:
    print('WHAT?')

# example2
age = int(input('Сколько Вам лет? '))
if age >= 18:
    print(f'Welcome {age}')
else:
    print(f'Good bye {18 - age}')

# example3
time = 10
if time < 12 or time > 13:
    print('WORK')
else:
    print('DINNER')

# example4
day = 'st'
if time >= 8 and day != 'su':
    print('OPEN')
else:
    print('CLOSE')

# example5
x = 7
if not x:
    print('OK')
else:
    print('NO')

# Пример 5
x = 1
print('OK' if x else 'NO')
res = 'OK' if x else 'NO'
print(res)
