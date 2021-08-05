def check_for_anagrams(a1, a2):
    if sorted(a1) == sorted(a2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")


s1 = "listen"
s2 = "silent"
check_for_anagrams(s1, s2)
# print(sorted(s1))
# anagrams - strings with same characters not necessarily in order.
