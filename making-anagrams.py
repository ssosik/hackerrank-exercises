#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    def makeAnagram(a, b):
    totalLen = len(b) + len(a)
    aCounts = Counter()
    bCounts = Counter()
    for c in a:
        aCounts[c] += 1
    for c in b:
        bCounts[c] += 1
    return sum([abs(aCounts[x] - bCounts[x]) for x in set(aCounts).intersection(bCounts)]) + sum([aCounts[x] for x in set(aCounts).difference(bCounts)]) + sum([bCounts[x] for x in set(bCounts).difference(aCounts)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

