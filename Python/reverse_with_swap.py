#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    l = []
    st = ""
    for i in sentence:
        if i == " ":
            l.append(st)
            st = ""
        else:
            st += i.swapcase()
            # continue
    l.append(st)
    st = ""
    l.reverse()
    news = ""
    for i in range(len(l)):
        if i != (len(l) - 1):
            news += l[i] + " "
        else:
            news += l[i]
    return news


sentence = input()
news = reverse_words_order_and_swap_cases(sentence)
print(news)
