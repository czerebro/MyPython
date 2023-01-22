# Булевый тип данных
my_true = True
my_false = False

print(type(my_false))  # <class 'bool'>
print(type(my_true))  # <class 'bool'>

# Приведение типов
# str() int() float() bool()
x = 5.2
print(x, type(x))
x = int(x)  # Не округляет а отбрасывает дробную часть
print(x, type(x))
x = str(x)
print(x, type(x))
x = bool(x)
y = 0
y = bool(y)
z = ''
z = bool(z)
w = None
w = bool(w)
print(x, type(x))  # True
print(y, type(y), z, type(z), w, type(w))  # False
