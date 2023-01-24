# Методы для работы со списками

l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
print(len(l))  # длина списка
print(l[4][0])
print(l[0:3])  # срез списка

names = ['Ivanov', 'Petrov', 'Sidorov']
print(names)
print(names[0])
print(names[1])
print(names[2])
names[2] = 'Fedorenko'
l[0:2] = [10, 15]
print(l)

# list.append(x) - Добавляет элемент в конец списка
names.append('new')
print(names)
# list.extend(L) - Расширяет список list, добавляя в конец все элементы списка L
l.extend([5, 7])
# Сложение списков
l2 = ['Hi', 19]
l += l2
print(l)
# list.insert(i, x) - Вставляет на i-ый элемент значение x
l.insert(2, 'test2')
print(l)
# list.remove(x) - Удаляет первый элемент в списке, имеющий значение x.
# ValueError, если такого элемента не существует
l.remove('world')
print(l)
# list.pop([i]) - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
test = l.pop()
print(l)
print(test)
test = l.pop(4)
print(l)
# list.index(x, [start [, end]]) - Возвращает положение первого элемента со значением x
# (при этом поиск ведется от start до end)
k = l.index(5)
print(k)
# list.count(x) - Возвращает количество элементов со значением x
l.count('Hi')
print(l.count('Hi'))
# list.sort([key=функция], [reverse=False]) - Сортирует список на основе функции
# значения списка должны быть однотипны
names.sort()  # буквы в алфавитном порядке
print(names)
test3 = sorted(names)  # равно names.sort()
print(test3)
names.sort(reverse=True)  # Разворот сортировки
print(names)
# list.reverse() - Разворачивает список
l.reverse()
print(l)
# list.copy() - Возвращает копию списка
l1 = names.copy()
print(l1)
# list.clear() - Очищает список
l1.clear()
print(l1)
