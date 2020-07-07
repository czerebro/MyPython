#string functions
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

s = 'Sergey Fedorenko'

#long string
print(len(s))

#Переводит первый символ строки в верхний регистр, а все остальные в нижний
print(s.capitalize())

#Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
print(s.center(20, '.'))

#Возвращает количество непересекающихся вхождений подстроки в диапазоне [начало, конец] (0 и длина строки по умолчанию)
print(s.count('e', 1, 10))

#Поиск подстроки в строке. Возвращает номер первого вхождения или -1
print(s.find('e'))

#Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
print(s.index('e'))

#(шаблон, замена) - Замена шаблона
print(s.replace('e', 'W'))

#([символ])- Разбиение строки по разделителю
print(s.split())
print(s.split(','))
print(s.split('e'))

#Состоит ли строка из цифр
print(s.isdigit())

#Состоит ли строка из букв
print(s.isalpha())

#Состоит ли строка из цифр или букв
print(s.isalpha())

#Состоит ли строка из символов в нижнем регистре
print(s.islower())

#Состоит ли строка из символов в верхнем регистре
print(s.isupper())

#Добавляет разделитель  для каждого элемента и формирует строку на выходе. На вход ждет строку
dots = '..'
my_str = dots.join(['1', '2'])  # '1..2'
print(my_str, type(my_str))
my_str = dots.join('ab')  # 'a..b'
print(my_str)

l1 = list(range(1, 10))  #[int]
l2 = list('hello')
print(l1)
print(l2)
#s1 = '-'.join(str)      #error
#Для массового приведения к строке можно воспользоваться функцией map():
# dots.join(map(str, [100, 200])) # '100..200'
s1 = '-'.join(map(str, l1))
s2 = ','.join(l2)
print(s1)
print(s2)

