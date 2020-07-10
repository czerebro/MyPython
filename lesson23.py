#dictionaries
#create
d = {}      #empty
product1 = {
    'title': 'Sony',
    'price': 100
}
product2 = dict(title='iPhone', price=110)  #конструктор
print(type(d))
print(product1)
print(product2)

#create from list
users = [
    ['bob@ya.ru', 'Bob'],
    ['den@ya.ru', 'Den'],
    ['ron@ya.ru', 'Ron'],
]
print(users)
d_users = dict(users)
print(d_users)

#create from кортеж
users2 = (
    ('bob@ya.ru', 'Bob'),
    ('den@ya.ru', 'Den'),
    ('ron@ya.ru', 'Ron'),
)
t_users = dict(users2)
print(t_users)

#create from
product3 = dict.fromkeys(['price1', 'price2', 'price3'], 50)
product_none = dict.fromkeys(['price1', 'price2', 'price3'])
print(product3)
print(product_none)

#генератор создания словаря
nums = {i: i + 1 for i in range(1, 10)}   #каждому элементу последовательности от 1 до 9 присваивается значение элемента +1
print(nums)

#operation on dic
print(product1['title'])
print(product1['price'])
print(product1.get('title'))
print(product1.get('title2'))  #None
print(product1.get('title2', ''))  #
print(product1.get('title2', 'No'))  #No
#print(nums['1'])       #error
print(nums[1])

#перебор словаря
for key in product1:
    print(key)
    print(product1[key])
    print(f'{key}: {product1[key]}')

#items возвращает пару ключ.значение
print(product1.items())
for key, value in product1.items():
    print(key, value)

#dict in dict
products = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 200},
    {'title': 'Samsung', 'price': 300},
]

print(products)

for product in products:
    print(product['title'], product['price'])