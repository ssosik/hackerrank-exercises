#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def findCommonSubstringCount(s1,s2):
    ret = 0
    for i in s1:
        for j in s2:
            if i == j:
                print(i,j)
                ret += 1
    return ret
    
def commonChild(s1, s2):
    intersection = set(s1).intersection(s2)
    s1matches = [c for c in s1 if c in intersection]
    s2matches = [c for c in s2 if c in intersection]
    if len(s1matches) < len(s2matches):
        return findCommonSubstringCount(s1matches,s2matches)
    else:
        return findCommonSubstringCount(s2matches,s1matches)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()

