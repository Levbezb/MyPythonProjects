if 1 == 1:                        # Пример того, как работает условный оператор if else в питоне 
    print('True')
else:
    print('False')


num = 10

if num > 1 and num < 200:         # В условном операторе if else есть логические операции and or и not  
    print('True')                 # Пример того, как они работают и пишутся
else:
    print('False')

if num > 1 or num == 0:
    print('True')
else:
    print('False')

if not (num < 0):                 # Логическая операция not действует также как минус в математике, то есть  
    print('True')                 # меняет все значения на противоположные: num >= 0
else:
    print('False')




if num < 200:                     # Пример вложенных условных операторов в питоне
    if num > 10:
        print('Yes')
    else:
        print('No')
else:
    print('Nan')


if num < 10:                      # Пример каскадного условия усл. опер. в питоне
    print('<10')                  # Не обязательно писать else в конце, если его не будет, цикл просто прекратится, ничего не сделав
elif num < 50:                    
    print('<50')
elif num < 150:
    print('<150')




string6 = 'qwertyuiop'
if 'w' in string6:                         # В Python есть специальный оператор in,
    print('yes')                           # который позволяет проверить, что одна строка находится внутри другой.


