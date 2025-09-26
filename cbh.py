# объявление функции
def draw_triangle():
    for i in range(8, 0, -1):
        for j in range(i):
            print(' ', end='')
        print((16-i-j) * '*')

# основная программа
draw_triangle()  # вызов функции