#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.

def sherlockAndAnagrams(s):
    count = 0
    # Gets count of each character
    dic = Counter(s)
    for i in range(2, len(s)):
        substring = s[0:i]
        l = len(substring)
        # Sort the substring alphabetically
        dic["".join(sorted(substring))] += 1
        # Gets other possible substrings of length l
        for j in range(1, len(s)):
            if j + l <= len(s):
                dic["".join(sorted(s[j:j+l]))] += 1
    # Formula to get number of anagrams based on number of substrings with matching length and characters
    for k, v in dic.items():
        count += (v * (v - 1)) // 2
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
