'''
case OS
devs: M.Kondrashov: 30%
      E. Bikmetov:
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
2. На уровень вверх
3. На уровень вниз
4. Количество файлов и каталогов
5. Размер текущего каталога (в байтах)
6. Поиск файла
7. Выход из программы
'''


def countBytes(path):
    """Размер файла"""
    print(os.path.getsize(path))

def moveUp():
    os.chdir(os.getcwd()[: - os.getcwd()[::-1].find('\\')])

def moveDown(currentDir):
    try:
        os.chdir(currentDir)
        print()
    except:
        print('Название папки введено неправильно')
        currentDir = input('Введите название заново: ')
        return moveDown(currentDir)

def countFiles(path):
    os.listdir(path)

def findFiles(target, path):
    try:
        for i in os.listdir(path):
            if i == target:
                return print(path + '\\' + i)
            if os.path.isdir(path + '\\' + i):
                findFiles(target, path + '\\' + i)

    except FileNotFoundError:
        print("Адрес каталога указан неверно")
        return ''

def runCommand(command):
    """Выполнить команду"""
    if command == 1:
        print('\n'.join(os.listdir()))
        print()
    if command == 2:
        moveUp()

    if command == 3:
        a = input('Введите название папки в которую нужно перейти: ')
        moveDown(os.getcwd() + '\\' + a)

    if command == 4:
        b = input('Укажите папку: ')

        countFiles(b)

    if command == 5:
        return countBytes(path=os.getcwd())

    if command == 6:
        t = input('Введите файл который нужно найти: ')
        p = input('Введите адрес каталога в котором нужно найти файл: ')
        ret = findFiles(t, p)
        if ret == '':
            print("Файл не найден")
        else:
            print(ret)
    if command == 7:
        print('Работа программы завершена')
        exit()


def main():
    """Основа программы"""
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)

main()

