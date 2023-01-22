#вывести содержимое папки и каталогов в виде древа
"""
    Адрес очередного каталога в виде строки.
    В форме списка имена подкаталогов первого уровня вложенности для данного каталога.
    В виде списка имена файлов данного каталога.
"""

import os

path = "C:\Intel"

arr = list(os.walk(path))

def scan_folder(folder):
    for root, dirs, files in arr:
        level_papki = root.count(os.sep)
        sdvig_papok = ' ' * 4 * level_papki
        sdvig_failov = ' ' * 4 * (level_papki + 1)
        print(f'{sdvig_papok}[{os.path.basename(root)}]')
        for file in files:
            print(f'{sdvig_failov}{file}')

scan_folder(path)

"""
arr = os.walk(path)
print(list(arr))

def folder_tree(folder):
    for root, dirs, files in os.walk(folder):
        if dir != '.git':
            level = root.replace(folder, '').count(os.sep)
            indent = '.' * 4 * (level)
            print('{}{}/'.format(indent, os.path.basename(root)))
            subindent = '.' * 4 * (level + 1)
            for f in files:
                print('{}{}'.format(subindent, f))


folder_tree(path)
"""

