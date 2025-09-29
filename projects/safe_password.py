from random import *

digits = '1234567890'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

count = int(input('Введите количество паролей: '))
length = int(input('Введите длину пароля: '))
with_digits = input('Включать ли цифры 1234567890? (да = д, нет = н): ')
with_upletters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да = д, нет = н): ')
with_lowletters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да = д, нет = н): ')
with_symbols = input('Включать ли символы !#$%&*+-=?@^_? (да = д, нет = н): ')
without_symbols = input('Исключать ли неоднозначные символы il1Lo0O? (да = д, нет = н): ')

if with_digits == 'д':
    chars += digits
if with_upletters == 'д':
    chars += uppercase_letters
if with_lowletters == 'д':
    chars += lowercase_letters
if with_symbols == 'д':
    chars += punctuation

def generate_password(length, chars):           # Функция генерирует пароли с указанными данными
    password = ''
    while length > 0:
        c = choice(chars)
        if without_symbols == 'д':
            if c in 'il1Lo0O':
                continue
        password += c
        length -= 1
    print(password)

for _ in range(count):
    generate_password(length, chars)

