#type Bool
my_true = True
my_false = False

print(type(my_false))
print(type(my_true))

#rechange type
#str() int() float() bool()
x = 5.2
print(x, type(x))
x = int(x)
print(x, type(x))
x = str(x)
print(x, type(x))
x = bool(x)
y = 0
y = bool(y)
print(x, type(x), y, type(y))