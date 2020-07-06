"""
Дан список words. Составьте из него список слов-палиндромов.
Попробуйте это сделать двумя способами: произвольное решение и решение в одну строчку кода.
Дан список my_str со строками, часть из которых являются палиндромами. Составьте новый список строк-палиндромов.
"""

#ver1
words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']

'''for i in words:
    newList = list((i))
    newList2 = list(newList)
    newList2.reverse()
    if newList != newList2:
        words.remove(i)
print(words)'''

#ver1.1

for i in my_str:
    new_str = [j for j in i.lower() if j != ' ']
    new_str2 = list(new_str)
    new_str2.reverse()
    if new_str != new_str2:
        my_str.remove(i)
print(my_str)





