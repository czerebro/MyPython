# Вывести таблицу умножения
# vertikal
'''
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')
    print('\n')
'''

# gorizontal
"""
for x in range(1, 11):
    for y in range(1, 11):
        z = y * x
        print(f'{y} * {x:>2} = {z:>3}', end='          ')
    print('\n', end='')
"""

# buitiful
for x in range(1, 11):
    for y in range(1, 6):
        z = y * x
        print(f'{y} * {x:>2} = {z:>3}', end='          ')
    print('\n', end='')

print('\n')

for x in range(1, 11):
    for y in range(6, 11):
        z = y * x
        print(f'{y} * {x:>2} = {z:>3}', end='          ')
    print('\n', end='')
