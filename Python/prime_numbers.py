num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            print("The entered number is not a prime.")
            break
    else:
        print("The entered number is a prime number.")

else:
    print("The entered number is not a prime.")
