#!/bin/python3
# IN PROGRESS

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0]*n
    print(queries)
    for sublist in queries:
        index1 = sublist[0] - 1
        index2 = sublist[1]
        add = sublist[2]
        for i in range(index1, index2):
            arr[i] += add  
        print(arr)
    return max(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
