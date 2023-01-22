#work with files
f = open('C:/file.txt', 'r', encoding='utf-8')
text = f.read(2)
text2 = f.read()
f.close()

print(f.encoding)
print(text)
print(text2)

lines = ['Новая строка 1', 'Новая строка 2']
f = open('C:/usr/file.txt', 'a', encoding='utf-8')
f.write('Новая строка\n')
for i in lines:                   # 1й вариант
    f.write(i + '\n')
f.writelines(f'{i}\n' for i in lines)               # 2й вариант
f.close()

f = open('C:/usr/file.txt', 'r', encoding='utf-8')
for line in f:
    print(line, end='\n')
    print(line, end='')
    print(line.replace('\n', ''))
f.close()

f = open('C:/usr/file2.txt', 'w', encoding='utf-8')
f.writelines(f'{i}\n' for i in lines)
f.close()