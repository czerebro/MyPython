# Операции со строками
s = 'C:\\Python38\\test.txt'
print(s)
s = r'C:\Python38\test.txt'  # не обрабатываются экранирующие последовательности
print(s)

# Склеивание строк (конкатенация)
s = 'Py' 'thon'
print(s)  # Python

s1 = 'Hello, '
s2 = 'world'
s3 = s1 + s2
print(s3)  # Hello, world

name = 'John'
age = 30
# print('My name is ' + name + " I'm " + age)   error
print('My name is ' + name + " I'm " + str(age))

# Повторение строк
print('Hello ' * 5)

# Индексация строк
'''
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9  10  11  12
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2 -1
'''
s4 = 'Hello world!'
print(s4[0], s4[9], s4[-1], s4[-6])  # H l ! w

# Срезы
# [x:y:z]  начало среза:конец среза:шаг среза
print(s4[0:12])  # =print(s4[::])
print(s4[0:5])  # =print(s4[:5])
print(s4[6:])  # =print(s4[6:12])
print(s4[::2])  # Пропустить каждый второй символ
print(s4[::-1])  # Перевернуть строку
print(s4[:5] + s4[6:])
print(s4[-1])  # =print(s4[-1:-12])
