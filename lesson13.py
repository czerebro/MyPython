#while
i = 2
while i <= 10:
    print(i, end=' ')
    i += 1        #i = i + 1

print('Sergey', 'Fedorenko', sep='.')

#for + continue
s = 'Hello world'
for l in s:                 #для каждой буквы в строке s
    if l == ' ':
        continue
    print (f'"{l}"', end=' ')

#for + break
for i in 'Hello world':
    if i == ' ':
        break
    print(i, end=' ')

#for + else
for i in 'HelloWorld':
    print(i, end=' ')
else:
    print(r'No spaces')
