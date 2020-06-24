#using string type
string1 = 'Hello'
string2 = "world"
print(string1, string2)

string1 = 'Hello, "world"!'
string2 =  "Hello, 'world'!"
print(string1, string2)

#ekranirovanie
string1 = "Hello, \"great\" 'world'!" #print " and '
string2 = "Hello, \\ 'world'!"        #print \
print(string1, string2)

string1 = "Hello, \t 'world'!" #tab
string2 = "Hello, \n 'world'!" #enter
print(string1, string2)

#multi string
stih = '''
Раз два три
Четыре пять
'''
print(stih)

stih = '''\
Раз два три
Четыре пять\
'''
print(stih)

stih = """
Раз два три
Четыре пять
"""
print(stih)

#logical string
#remove on next string but it is one string
stih1 = 'Раз два три' \
        ' четыре пять'