#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import string


def missingCharacters(s):
    # Write your code here
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    numb = []
    alphabet_string = string.ascii_lowercase
    alphabet_list = list(alphabet_string)
    alpha = []
    for i in s:
        if i in num:
            numb.append(i);
        elif i in alphabet_list:
            alpha.append(i)
    new_s = ""
    for i in num:
        if i in numb:
            continue
        else:
            new_s += i
    for i in alphabet_list:
        if i in alpha:
            continue
        else:
            new_s += i
    return new_s


sentence = input()
news = missingCharacters(sentence)
print(news)
