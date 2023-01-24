# Списки = массивы
# Можно хранить разнотипные данные
l = [1, 2, 3, 'Hello', ['test', 10], True]
print(type(l))  # <class 'list'>

# Варианты создание списков
l2 = list('hello')  # ['h', 'e', 'l', 'l', 'o']
l3 = list((1, 2, 3))  # Кортеж [1, 2, 3]
# каждую итерацию перебирается побуквенно hello world. буква помещается в список если не равна пробелу
l4 = [i for i in 'hello world' if i != ' ']
# каждую итерацию перебирается побуквенно hello world. буква помещается в список если не равна символам из списка
l5 = [i for i in 'hello world' if i not in ['l', 'e', ' ', 'o']]
# задвоение букв
l6 = [i * 2 for i in 'hello world' if i not in ['l', 'e', ' ', 'o']]
l7 = [i for i in l]  # create list from copy l
l8 = list(range(1, 10))
print(l2, l3, l4, l5, l6, l7, l8, sep='\n')  # list 1-9

# Создание списка через генератор range()
print(type(range(3)))
print(list(range(3)))  # [0, 1, 2]
print(list(range(1, 5)))  # [1, 2, 3, 4]
print(list(range(0, 11, 2)))  # [0, 2, 4, 6, 8, 10]

# Вложенные циклы
for i in range(1, 3):
    print(f'внешний цикл #{i}')
    for j in range(1, 3):
        print(f'\tвнутренний цикл #{j}')
