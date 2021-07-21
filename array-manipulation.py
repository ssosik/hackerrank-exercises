#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulationX(n, m, queries):
    maxx = 0
    row = [0 for _ in range(n)]

    for q in queries:
        start = q[0] - 1
        end = q[1] - 1
        val = q[2]
        for i in range(n):
            if i >= start and i <= end:
                row[i] += val
        maxx = max(*row, maxx)

    return maxx

# taken from: https://www.thepoorcoder.com/hackerrank-array-manipulation-solution/

from collections import Counter

def arrayManipulation(n, queries):
    c = Counter()
    for a,b,k in queries:
        c[a]  +=k
        c[b+1]-=k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum+= c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, m, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
