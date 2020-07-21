#оформить решение задачи по рисованию таблицы умножения в виде функции
#buitiful

def draw_table(a, b):
    for x in range(1, 11):
        for y in range(a, b):
            z = y * x
            print(f'{y} * {x:>2} = {z:>3}', end='          ')
        print('\n', end='')

draw_table(1, 6)
print('\n')
draw_table(6, 11)