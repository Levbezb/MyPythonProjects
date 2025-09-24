# Этот код выводит число в диапазоне от a до b с максимальной суммой делителей
# <число с максимальной суммой делителей> <сумма делителей этого числа>

a, b = int(input()), int(input())
total1 = 0
count1 = 0
for i in range(a, b+1):
    total = 0
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count = i
            total += j
    if total >= total1 and count > count1:
        total1 = total
        count1 = count
print(count1, total1)