# pizzaforces problem in codeforces

t = int(input())
for _ in range(t):
    n = int(input())
    rem = n % 6
    div = n // 6
    t = 0
    if n <= 6:
        t = 15
    elif rem == 0:
        t = div * 15
    elif rem != 0 and rem <= 2:
        t = (div * 15) + 5
    elif rem != 0 and rem <= 4:
        t = (div * 15) + 10
    else:
        t = (div + 1) * 15
    print(t)
