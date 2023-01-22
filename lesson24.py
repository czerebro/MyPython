#functions of dict
product1 = {'title': 'Sony', 'price': 100}
# dict.clear() - очищает словарь
# dict.copy() - возвращает копию словаря
print(product1.copy())
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None)
print(product1.get('price'))
# dict.items() - возвращает пары (ключ, значение)
print(product1.items())
# dict.keys() - возвращает ключи в словаре
print(product1.keys())
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение)
print(product1.pop('title', 'NO'))  #если ключа нет выведет NO
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены
print(product1.popitem())
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None)
product1 = {'title': 'Sony', 'price': 100}
print(product1.setdefault('title')) #если ключ есть - выводит значение
print(product1)
#print(product1.setdefault('title2'))  #если ключа нет - добавляет его в словарь со значением None
print(product1.setdefault('title2', 'test'))  #если ключа нет добавит его в словарь со значением test
print(product1)
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из другого словаря. Существующие ключи перезаписываются. Возвращает None (не новый словарь!)
product1 = {'title': 'Sony', 'price': 100}
product1.update({'test': 'value'})
product1.update({'price': 200})
print(product1)
# dict.values() - возвращает значения в словаре
print(product1.values())




