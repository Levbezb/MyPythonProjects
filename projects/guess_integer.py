from random import *

rng_numbers = 100
cnt = 0

def make_range():               # Функция отвечает за указание правой границы, если пользователь захочет выставить свой диапазон чисел
    while True:
        global rng_numbers
        rng_numbers = input('Укажите правую границу: ')
        if rng_numbers.isdigit():
            rng_numbers = int(rng_numbers)
            break
        else:
            print('А может быть все-таки введем целое число?')


print('Добро пожаловать в числовую угадайку!')

rng = input('Хотите выбрать диапазон чисел угадайки? Если да, введите "д", если нет, введите "н": ')
if rng == 'д':
    make_range()

n = randint(1, rng_numbers)

def is_valid(number):                                           # Функция проверяет число на то, что оно действительно число и лежит в 
    if  number.isdigit() and 1 <= int(number) <= rng_numbers:   # диапазоне от 1 до указанной правой границы
        return True
    else:
        return False

while True:
    num = input(f'Введите число от 1 до {rng_numbers}: ')

    if is_valid(num):
        num = int(num)
    else:
        print(f'А может быть все-таки введем целое число от 1 до {rng_numbers}?')
        continue
    if num < n:
        cnt += 1
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif num > n:
        cnt += 1
        print('Ваше число больше загаданного, попробуте еще разок')
    elif num == n:
        cnt += 1
        print(f'Поздравляю! вы угадали число {n} за {cnt} попыток')

        replay = input('Если хотите сыграть еще раз, введите "д", если нет, введите "н": ')     # Переигровка
        if replay == 'д':
            rng_numbers = 100

            rng = input('Хотите выбрать диапазон чисел угадайки? Если да, введите "д", если нет, введите "н": ')
            if rng == 'д':
                make_range()

            n = randint(1, rng_numbers)
            cnt = 0
            continue
        else:
            break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
