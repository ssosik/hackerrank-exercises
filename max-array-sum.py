#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    pass

def getIndexes(n):
    idxs = set([(i,) for i in range(0, n, 1)])
    for x in range(2, n, 1):
        for y in range(0, x, 1):
            idxs.add(tuple([i for i in range(y, n, x)]))

    return idxs

if __name__ == '__main__':
    print(getIndexes(6))
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #arr = list(map(int, input().rstrip().split()))

    #res = maxSubsetSum(arr)

    #fptr.write(str(res) + '\n')

    #fptr.close()

