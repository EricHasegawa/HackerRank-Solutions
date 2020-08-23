#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    for i in range(0, len(arr)):
        while arr[i] != i + 1:
            temp = arr[arr[i] - 1] # set temp to be the previous element
            arr[arr[i] - 1] = arr[i] # set previous element to current element
            arr[i] = temp # set current element to previous element
            swaps += 1
    return swaps        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
