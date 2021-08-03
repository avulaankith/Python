# finding the number of times a given substring is present in the string entered.


st = input("Enter the string: ")
subst = input("Enter the sub string to be searched: ")
# st = "abcdcdcd"
# subst = "cd"
l = len(subst)
count = 0
for i in range(len(st)-l+1):
    # print(st[i:i+l])
    if subst == st[i:i + l]:
        count += 1
print(count)
