# Of the N people, take those N people in the form of an array A.Out of the invited persons a person can be friends
# with the persons where A[i] % A[j] == 0 or A[j] % A[i] == 0. find maximum number of friends each person can make?
# A[i] denotes the trust value of each person. A is the array which stores the trust value.

lt = input().split()
lst = []
for i in lt:
    lst.append(int(i))

n = len(lst)

fr_lst = []

for i in range(n):
    friend_number = 0
    for j in range(n):
        if i != j:
            if ((lst[i] % lst[j]) == 0) or ((lst[j] % lst[i]) == 0):
                friend_number += 1

    fr_lst.append(friend_number)


print(fr_lst)
