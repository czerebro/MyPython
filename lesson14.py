#spiski = massivi
l = [1, 2, 3, 'Hello', ['test', 10], True]
print(type(l))

#create list
l2 = list('hello')
l3 = list((1, 2, 3))
l4 = [i for i in 'hello world' if i != ' '] #каждую итерацию перебирается побуквенно hello world. буква помещается в список если не равна пробелу
l5 = [i for i in 'hello world' if i not in ['l', 'e', ' ', 'o']]
l6 = [i * 2 for i in 'hello world' if i not in ['l', 'e', ' ', 'o']]
l7 = [i for i in l]         #create list from copy l
l8 = list(range(1, 10))
print(l2, l3, l4, l5, l6, l7, l8, sep='\n')  #list 1-9

#create range
print(type(range(3)))
print(list(range(3)))
print(list(range(1, 5)))
print(list(range(0, 11, 2)))

#for to for
for i in range(1, 3):
    print(f'внешний цикл #{i}')
    for j in range(1, 3):
        print(f'\tвнутренний цикл #{j}')