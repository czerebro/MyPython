"""
1. Дан список. Получите новый список, в котором каждое значение будет удвоено:
[1, 2, 3] --> [2, 4, 6]
"""

l2 = [1, 2, 3]
l4 = []
for i in range(0, len(l2)):
    l4.append(l2[i] * 2)
print(l4)

# l1 = [1, 2, 3]
# l2 = [i * 2 for i in l1]
# print(l2)

"""
2. Дан список. Возведите в квадрат каждый из его элементов и получит сумму всех полученных квадратов:
[1, 2, 3] --> 14 --> 1^2 + 2^2 + 3^2 = 14
"""

l = [1, 2, 3]
k = 0
for i in range(0, len(l)):
    k = k + l[i] * l[i]
print(k)

# l1 = [1, 2, 3]
# res = 0
# for num in l1:
#     res += num ** 2
# print(res)

"""
3. Игорь любит кататься на велосипеде. Он знает, что при этом важно не допустить обезвоживания и пьет 0,5 литра воды в час. 
Вам дается время в часах, и вам нужно вернуть количество литров, которые Игорь выпьет, с округлением до наименьшего значения.
time1 = 3 --> litres = 1
time2 = 6.7 --> litres = 3
time3 = 11.8 --> litres = 5
"""

time = float(input("Введите время: "))
litr = time * 0.5
print(f"За {time}ч выпито {int(litr)}л")

# time1 = 3 # litres = 1
# time2 = 6.7 # litres = 3
# time3 = 11.8 # litres = 5
#
# print(int(time1 // 2))
# print(int(time2 // 2))
# print(int(time3 // 2))
#
# print(int(time1 / 2))
# print(int(time2 / 2))
# print(int(time3 / 2))

"""
4. Дана строка 'Hello world'. Проверьте, если в этой строке есть символ пробела - " ", тогда преобразуйте строку к верхнему регистру, если же нет, тогда к нижнему.
***************
s = 'Hello world'
if stm:
	pass
else:
	pass
"""

s = 'Hello world'
for l in s:
    if l == ' ':
        print(s.upper())
    else:
        print(s.lower())

#s = 'Hello world'
#if ' ' in s:
#    s = s.upper()
#else:
#    s = s.lower()
#print(s)