#format string
name = 'Sergey Fedorenko'
age = 33

print('My name is ' + name + '. I\'m ' + str(age))
print('My name is %(name)s. I\'m %(age)d' %{'name': name, 'age': age})   #old style
print('My name is %s. I\'m %d' %(name, age))
print('My name is %s. I\'m %d' %('David', age))

print('Title: %s, Price: %.2f' %('Sony', 40))


print('My name is {}. I\'m {}'.format(name, age))    #middle style
print('My name is {1}. I\'m {1}'.format(name, age))  #position for 0 to end
print('My name is {x}. I\'m {y}'.format(x=name, y=age))

print(f'My name is {name}. I\'m {age}')     #new style f-string
print(f'My name is {name}. I\'m {age + 7}')
print('5 + 2 = {}'.format(5 + 2))
print(f'5 + 2 = {5 + 2}')