#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sums = []
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            top_row = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            middle_row = arr[i + 1][j + 1]
            bottom_row = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            sums.append(top_row + middle_row + bottom_row)
            j += 1
        i += 1
    return max(sums)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
