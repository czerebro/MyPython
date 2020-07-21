#commenting functions
def get_sum(a, b):     # push Ctrl + Q
    """
    Return sum a and b.

    :param a:  First operand
    :type a: int
    :param b:  Second operand
    :type b: int
    :return:   Return sum a + b type int
    """
    return a + b


print(get_sum(1, 2))

#области видимости
a = 5   #global
def f():
    a = 10 #local
    a += 1
    print(a)
print(a)  #5
f()         #11
print(a)    #5

print('************')

def b():
    global a
    a += 1
    print(a)
print(a)  #5
b()         #6
print(a)    #6

print('************')

#func return func
l = [1, '2', 3]

def ff(l):
    return [i * 2 for i in l]

print(ff(l))

#ff = f2
def f2(l):
    def get_mult(x):
        if isinstance(x, int):          #isinstance проверяет операнд на принадлежность к типу
            return x * 2
    return [get_mult(i) for i in l if get_mult(i)]  #для каждого i в списке l запускаем get_mult() в том случае если это не None
    #return list(map(get_mult, l)
print(f2(l))

def f3(l):
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))
print(f3(l))