from random import *

n = randint(1, 100)

print('Добро пожаловать в числовую угадайку')

def is_valid(number):
    if  number.isdigit() and 1 <= int(number) <= 100:
        return True
    else:
        return False

while True:
    num = input('Введите число от 1 до 100: ')
    if is_valid(num):
        num = int(num)
    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
    if num < n:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num > n:
        print('Ваше число больше загаданного, попробуте еще разок')
    elif num == n:
        print(f'Поздравляю! вы угадали число {n}')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
