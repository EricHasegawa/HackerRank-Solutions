#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    min_bribes = 0
    for i in range(0, len(q)):
        if q[i] > i + 3:
            print("Too chaotic")
            return
        for j in range(q[i] - 2, i):
            if q[j] > q[i]:
                min_bribes += 1 
    print(min_bribes - 1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
