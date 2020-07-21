#owm functions
def hello(name, word):
    print(f'Hello {name}. Say {word}')

hello('Sergey', 'Hello')
hello(777, 'John')


def get_sum(a, b):
    print(a + b)

def new_sum(a, b):
    return a + b

x = 5
y = 8
get_sum(1, 3)
get_sum(x, y)

res = new_sum(x, y)
print(res)


def test_def():
    print('test')
print(test_def())     #test   None