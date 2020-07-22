"""
0. Задание от Санька. Переписать фукцию ниже
"""
def func(l1):
    l2 = []
    for item in l1:
        if item < 10:
            l2.append(item)
    return l2


def ff(l1):
    return [i for i in l1 if i < 10]


x = func([1, 15, 9])
y = ff([1, 18, 6, 16])
print(x)
print(y)

"""
1. Дан массив, в котором среди прочих элементов есть слово "odd" (нечетный). 
Определите, есть ли в списке число, которое является индексом элемента "odd". 
Напишите функцию, которая будет возвращать True или False, соответсвенно.
"""

def odd_ball(arr):
    return bool([item for item in arr if item == arr.index('odd')])

print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",10,"odd",3,"even"])) # True
print(odd_ball(["even",4,"even",7,"even",55,"even",6,"even",9,"odd",3,"even"])) # False
print(odd_ball(["even",10,"odd",2,"even"])) # True


"""
2. Напишите функцию find_sum(n), где аргумент функции - это конечный элемент последовательности включительно. 
Функция должна вернуть сумму всех чисел последовательности, кратных 3 или 5. 
Попробуйте решить задачу двумя способами (один из способов в одну строчку кода).
"""

def find_sum(n):
    pass

find_sum(5) # return 8 (3 + 5)
find_sum(10) # return 33 (3 + 5 + 6 + 9 + 10)


"""
3. Дан список имен. Выберите в новый список только те имена, которые состоят из 4-х букв.
names = ["Ryan", "Kieran", "Mark", "John", "David", "Paul"] # ["Ryan", "Mark", "John", "Paul"]
"""


def get_names(names):
    pass



