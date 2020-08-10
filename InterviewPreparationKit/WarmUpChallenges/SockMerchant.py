import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    for sock in ar:
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1
    total = 0
    for model in socks.values():
        if model % 2 == 0:
            total += model // 2
        else:
            total += (model - 1) // 2
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
