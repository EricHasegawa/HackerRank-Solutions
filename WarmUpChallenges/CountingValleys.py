#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    route = list(s)
    elevation = 0
    valleys = 0
    for direction in route:
        if elevation == 0:
            sea_level = True
        else:
            sea_level = False
        if direction == 'U':
            elevation += 1
        elif direction == 'D' and sea_level:
            valleys += 1
            elevation -= 1
        else:
            elevation -= 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
