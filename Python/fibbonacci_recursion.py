def fibonacci_series(n):
    if n < 0:
        print("Incorrect Input")
    elif n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)


i = int(input("Enter the index for the fibonacci number to find it: "))
print(fibonacci_series(i))
