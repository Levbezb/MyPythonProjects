n = int(input())
total = 0
for i in range(n, 0, -1):
    for j in range(i, n+1):
        total += 1
        print(total, end=' ')
    print()