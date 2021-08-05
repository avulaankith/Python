num = 1634

# Changed num variable to string,
# and calculated the length (number of digits)
order = len(str(num))
# so the value of order is 4

# initialize sum
sumi = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sumi += digit ** order
    temp //= 10

# display the result
if num == sumi:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
