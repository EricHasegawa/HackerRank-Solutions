#!/bin/python3

import math
import os
import random
import re
import sys
import itertools as it

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    # SLOW SOLUTION
    # arr = [0]*n
    # for sublist in queries:
    #     index1 = sublist[0] - 1
    #     index2 = sublist[1]
    #     add = sublist[2]
    #     for i in range(index1, index2):
    #         arr[i] += add  
    # return max(arr)

    #FASTER SOLUTION
    q = it.chain.from_iterable([(a, k), (b, -k)] for a, b, k in queries)
    return max(it.accumulate(c for _, c in sorted(q, key=lambda x: (x[0], -x[1]))))

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
