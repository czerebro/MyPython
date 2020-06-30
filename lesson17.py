#изменяемые и неизменяемые типы данных
#изменяемые
x = 10
print(x, id(x))
x = 20
print(x, id(x))

s = 'hello'
print(s, id(s))
s += 'world'
print(s, id(s))

#неизменяемые
l = [1, 2, 3]
print(l, id(l))
l.append(5)
print(l, id(l))

x = 10
y = x             #разные объекты
print(x, id(x))
print(y, id(y))

x = 15
print(x, id(x))
print(y, id(y))

l1 = [1, 2, 3]
print(l1, id(l1))
l2 = l1           #один и тот же объект
l3 = l1.copy()
l4 = l1[:]
print(l2, id(l2))
l1.append(5)
print(l1, id(l1))
print(l2, id(l2))
print(l3, id(l3))
print(l4, id(l4))

x = 10
print(x)
del x
#print(x) #error