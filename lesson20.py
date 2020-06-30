#kortezhi = tuple
t1 = (1, 2, 3)   #recommend
tt = (1, 2, 3, )
t2 = 1, 2, 3   #упаковка
x, y, z = t2   #распаковка
print(x, y, z)
tuple1 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
print(type(t1))
print(type(t2))
print(type(tt))
print(type(tuple1), id(tuple1), tuple1)
t = (2)
print(type(t))   #!!!!! int
t = (2, )
print(type(t, ))   #!!!!! tuple

#create tuple
t3 = tuple((1, 2, 3))
t4 = ()
t5 = tuple('Hello')
print(t3, t4, t5, sep='\n')
print(t5[2])


#example
list1 = [1, 2, 3]
tuple2 = (1, 2, 3)
print(list1.__sizeof__())      #bytes
print(tuple2.__sizeof__())     #bytes

a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

#operations
#add
t6 = tuple('Hello')
t7 = tuple(' world')
t8 = t6 + t7
print(t8)

#long
print(len(t8))

#количество элементов в последовательности
print(t8.count('l'))

#позиция символа в последовательности (символ, старт, стоп)
#если символа нет будет ошибка. обходим через условие
if 'l' in t8:
    print(t8.index('l'))
else:
    print(None)

for i in t8:
    if i == ' ':
        continue
    print(f'"{i}"', end=' ')

#обращение к элементам
#tuple1[0] = 'new'       error!!!
tuple1[4][0] = 'new'
print('\n', tuple1, id(tuple1))
tuple1[4].append('sergey')
print(tuple1, id(tuple1))



