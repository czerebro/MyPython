#множества set
#create sets
s1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
s2 = set('hello')    #конструтор
s3 = {i for i in range(1, 11)}
s4 = {5, 3, 10, 1, 9, 2}
s5 = set()              #empty
print(type(s1), s1)   #генератор
print(s2)
print(s3)
print(s4)
print(s5)

nums = [1, 2, 3, 3, 1, 2, 4, 5]
nums2 = list(set(nums))
print(nums2)

#example
a = set('abrakadabra')
b = set('alakazam')
print(a, b, sep='\n')

#sub - убираем из А буквы которые сть в Б
c = a -b
print(c)

#объединение
d = a | b
print((d))

#пересечение = дубли
e = a & b
print(e)

#множество из элементов - буквы в А или Б, но не в обоих, кроме дублей
f = a ^ b
print(f)

#functions
# set.copy() - возвращает копию множества
s6 = s1.copy()
print(s1, id(s1))
print(s6, id(s6))
# set.add(elem) - добавляет элемент в множество
s1.add('melon')
print(s1)
s1.add('apple')
print(s1)
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует
s1.remove('apple')
print(s1)
# set.discard(elem) - удаляет элемент, если он находится в множестве
s1.discard('melon')
print(s1)
# set.pop() - возвращает и удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
print(s1.pop())
print(s1)
# set.clear() - очистка множества
s1.clear()
print(s1)

#замороженое множество frozenset  - неизменяемое
a = frozenset('hello')
print(a)

#operations at set
s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for i in s:
    print(i)