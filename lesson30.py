#library of python
# https://docs.python.org/3/library/

import os               # work with operation system
#import random           #library generation random
#import random as r     #alias of random library
#from random import *
from random import randint, shuffle    #import 1 function shuffle

print(os.getcwd())     #current word directory
print(randint(1, 100))     #generation random int number

l = [1, 2, 3, 4, 5]
shuffle(l)
print(l)


import libs                 #own library
print(libs.get_count('hello', 'l'))
print(libs.get_len('hello'))
#print(__name__)    #имя файла если он откуда то подключается

f = libs.get_count
print(f('hello', 'l'))           #f = function get_count