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

