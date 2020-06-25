#Вывести год от 1900 до 2019 в строчку используя циклы
start = int(input("Введите начальный год: "))
end = int(input("Введите конечный год: "))
if start > end:
    print("Начальный год должен быть больше конечного")
else:
    while start <= end:
        print(start, end=' ')
        start += 1
