t = int(input())

for _ in range(t):
    word = input()
    l = len(word)
    if l <= 10:
        print(word)
    else:
        new_word = word[0] + str(len(word) - 2) + word[-1]
        print(new_word)
