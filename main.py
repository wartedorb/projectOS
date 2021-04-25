'''
case OS
devs: M.Kondrashov: 30%
      E. Bikmetov: 30%
      K. Bychkov:
'''

import os


def acceptCommand():
    """Запрос номера команды"""
    try:
        number = int(input('Выберите пункт меню: '))
        if 1 <= number <= 7:
            return number
        else:
            print('Такой команды нет.')
            return acceptCommand()
    except ValueError:
        print('Введите целое число.')
        return acceptCommand()


MENU = '''1. Просмотр каталога
2. На уровени вверх
3. На уровень вниз
4. Количество файлов и каталогов
5. Размер текущего каталога (в байтах)
6. Поиск файла
7. Выход из программы
'''


def countBytes(path):
    """Размер файла"""
    print(os.path.getsize(path))


def runCommand(command):
    """Выполнить команду"""
    if command == 5:
        return countBytes(path=os.getcwd())


def main():
    """Основа программы"""
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        if command == 7:
            print('Работа программы завершена')
            break


