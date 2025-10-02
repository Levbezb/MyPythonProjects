# Программа может зашифровать или расшифровать сообщение в шифре цезаря
print('Добро пожаловать, что вы хотите сделать? (введите цифру):')

def get_number():
    number = input('Пожалуйста, введите ключ (шаг сдвига): ')
    while True:
        if number.isdigit():
            return int(number)
        else:
            number = input('Пожалуйста, введите ЧИСЛО: ')


def get_desition():
    while True:
        what_to_do = input('1. шифровать строку \n2. дешифровать строку \n')
        if what_to_do == '1' or what_to_do == '2':
            return what_to_do
        else:
            print('Пожалуйста, введите цифру!')


def get_language():
    while True:
        language = input('На каком языке вы хотите обрабатывать запрос? (русский = рус, английский = анг): ')
        if language == 'рус' or language == 'анг':
            return language
        else:
            print('Пожалуйста, введите актуальный язык!')


def cipher(mes, shift):
    if language == 'анг':
        result = "" 
        for c in mes:
            if c.isalpha():
                if c.islower():
                    result += chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
                else:
                    result += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += c
        return result
    
    elif language == 'рус':
        result = "" 
        for c in mes:
            if c.isalpha():
                if c.islower():
                    result += chr((ord(c) - ord('а') + shift) % 33 + ord('а'))
                else:
                    result += chr((ord(c) - ord('А') + shift) % 33 + ord('А'))
            else:
                result += c
        return result
    

def decipher():
    if language == 'анг':
        for shift in range(26):
            print(f'Ключ {shift}: {cipher(message, shift)}')
    elif language == 'рус':
        for shift in range(33):
            print(f'Ключ {shift}: {cipher(message, shift)}')



def contin():
    text = input('Еще вопросы? (да/нет): ')
    return text.lower() == 'да'

keep_working = True

while keep_working:
    what_to_do = get_desition()

    if what_to_do == '1':
        language = get_language()
        message = input('Пожалуста, введите строку для шифрования: \n')
        shift = get_number()
        print(cipher(message, shift))

    elif what_to_do == '2':
        language = get_language()
        message = input('Пожалуста, введите строку для дешифрования: \n')
        decipher()

    keep_working = contin()



