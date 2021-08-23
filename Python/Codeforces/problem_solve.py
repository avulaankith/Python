t = int(input())
count = 0
for _ in range(t):
    # lcount = 0
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    s = a + b + c

    if s > 1:
        count += 1

print(count)
