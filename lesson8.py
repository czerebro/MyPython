# Строковый тип данных
# Объявление строк
string1 = 'Hello'
string2 = "world"
print(string1, string2)

# Кавычки внутри кавычек
string1 = 'Hello, "world"!'
string2 = "Hello, 'world'!"
print(string1, string2)

# Экранирование кавычек
string1 = "Hello, \"great\" 'world'!"
string2 = "Hello, \\ 'world'!"
print(string1, string2)

# Экранирующие последовательности
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-literaly-strok.html
string1 = "Hello, \t 'world'!"  # tab
string2 = "Hello, \n 'world'!"  # enter
print(string1, string2)

# Многострочность
stih = '''
Раз два три
Четыре пять
'''
print(stih)

# ставим \ чтобы убрать лишний перенос строки в начале и конце
stih = '''\
Раз два три
Четыре пять\
'''
print(stih)

stih = """
Раз два три
Четыре пять
"""
print(stih)

# Логическая строка
# Две физические строки воспринимаются как одна логическая
stih1 = 'Раз два три\n' \
        'четыре пять'
stih2 = ('Раз два три\n'
         'четыре пять')
print(stih1)
print(stih2)

# Вывод символов Unicode
print('\u2588')
print('\u2591')
