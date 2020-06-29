#using if
print(2 > 3)
print(2 < 3)
print(2 != 3)
print( 2 == 3)
print('h' > 'a') #True

'''
if выражение 1:
    блок кода 1
elif выражение 2:
    блок кода 2
else:
    блок кода 3
'''

#example false
x = 0
if x:
    print("переменная х истинно")
else:
    print("переменная х ложно")

#example true
if 5:
    print("переменная х истинно")
else:
    print("переменная х ложно")

#example1
light = 'red'
if light == 'red':
    print('STOP')
elif light == 'yellow':
    print('WAIT')
elif light == 'green':
    print('GO')
else:
    print('WHAT?')

#example2
age = int(input('Сколько Вам лет? '))
if age >= 18:
    print(f'Welcome {age}')
else:
    print(f'Good bye {18 - age}')

#example3
time = 11
if time < 12 or time >  13:
    print('DINNER')
else:
    print('WORK')

#example4
day = 'st'
if time > 8 and day != 'su':
    print('OPEN')
else:
    print('CLOSE')

#example5
x = 7
if not x:
    print('OK')
else:
    print('NO')

# example5
x = 1
res = 'OK' if x else 'NO'
print(res)