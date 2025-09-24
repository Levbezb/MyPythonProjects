    # опровержение гипотезы эйлера о сумме степеней, без оптимизации,  работает примерно 2-5 минут
for e in range(1, 151):
    for a in range(1, e-1):
        for b in range(a, e-1):
            for c in range(b, e-1):
                for d in range(c, e-1):
                    if a**5 + b**5 + c**5 + d**5 == e**5:
                        print(a+b+c+d+e)
