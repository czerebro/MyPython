#using arguments of functions
def get_sum(a, b, c=1, d=6):   #c и d именованные аргументы
    return a + b + c + d
print(get_sum(1, 3, 5, 7))     #16
print(get_sum(1, 3))           #11
print(get_sum(1, 3, 8))           #18
print(get_sum(1, 3, d=1))           #6

#произвольное количество аргументов
#def get_add(*args, **kwargs):             # * - кортеж,   ** - словарь
#    pass

def get_add(*args):
    return sum(args)

get_add(1, 5, 10)
print(sum([1, 4, 5]))  #10
print(get_add(1, 4, 5)) #10

def func(**x):
    print(x)
func(a=1, b=4, c=5)

def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
f(1, 2, 3, 4, x='test', y='Hello')
f(1, 2)