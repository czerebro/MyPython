# Форматирование строк
name = 'Sergey Fedorenko'
age = 33

print('My name is ' + name + '. I\'m ' + str(age))  # строка без форматирования
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})  # форматирование именными маркерами
print('My name is %s. I\'m %d' % (name, age))  # форматирование позиционными маркерами
print('My name is %s. I\'m %d' % ('David', age))

print('Title: %s, Price: %.2f' % ('Sony', 40))  # Форматирование для Float с 2мя знаками после запятой

print('My name is {}. I\'m {}'.format(name, age))  # Форматирование через метод format
print('My name is {1}. I\'m {1}'.format(name, age))  # Форматирование с указанием позиции подстановки (начинаются с 0)
print('My name is {x}. I\'m {y}'.format(x=name, y=age))  # Форматирование с именными аргументами
print('5 + 2 = {}'.format(5 + 2))  # Математические операции

# F-строки
print(f'My name is {name}. I\'m {age}')
print(f'My name is {name}. I\'m {age + 7}')
print(f'5 + 2 = {5 + 2}')  # Математические операции
