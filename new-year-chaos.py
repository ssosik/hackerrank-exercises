#!/bin/python3

import math
import os
import random
import re
import sys
import pdb

# https://www.hackerrank.com/challenges/new-year-chaos?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
def minimumBribes(l, q):
    cnt = 0
    # Start from the back of the queue and work our way to the front, counting
    # the number of cuts that took place
    for i in range(l, 0, -1):
        # Find the index in the queue for the current item
        idx = q.index(i) 
        if i - (idx + 1) > 2: # Need ABS here?
            # Check if the current item is more than 2 spaces away from where it
            # belongs; is so error
            print('Too chaotic')
            return
        elif i != idx + 1:
            # If the current item is out of place, determine how many cuts took
            # place and put it back its original location
            cnt += i - (idx + 1)
            q.pop(idx)
            q.insert(i-1, i)
        print(q)
    print(cnt)

if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print(q)
    minimumBribes(8, q)
