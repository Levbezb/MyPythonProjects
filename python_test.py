name = input('Введите ваше имя: ')
print('Здравствуйте, ', name, ', ','Введите ваш возраст: ', sep='', end=' ')
age = int(input())
if age < 18:
    print('Вам отказано в доступе')
else:
    print('Доступ разрешен')


