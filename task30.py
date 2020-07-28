#изменить игру угадай число используя библиотеки питона из task24
#добавить команды продолжения или прекращения игры по кнопка y/n
from random import randint
secret = randint(1, 100)
popitka = 0
number = 0
while secret != number:
    number = int(input('Введите число от 1 до 100: '))
    popitka += 1
    if number == secret:
        print(f"Поздравляю! вы угадали число за {popitka} попытки")
        if input("Хотите поиграть еще? (y/n)") == 'y':
            secret = randint(1, 100)
            popitka = 0
    elif number > secret:
        print('Загаданное число меньше Вашего')
    elif number < secret:
        print('Загаданное число больше Вашего')
