import math
import os
import random
import re
import sys
from collections import Counter, defaultdict

def countTriplets(arr, r):
    cnt = 0
    left = Counter()
    right = Counter()

    i = arr[0]
    left[i] += 1

    j = arr[1]

    for k in arr[2:]:
        right[k] += 1

    i = int(j/r)
    k = int(j*r)
    cnt += left[i] * right[k]
    print(cnt)
    for x in range(2, len(arr) - 1):
        print(x, j)
        i = int(j/r)
        k = int(j*r)
        cnt += left[i] * right[k]
        print(cnt)

        left[j] += 1
        j = arr[x]
        right[j] -= 1

    return cnt
        
def countTripletsBetter(arr, r):
    cnt = 0
    left = Counter()
    right = Counter()

    i = arr[0]

    left[i] += 1
    for k in arr[2:]:
        right[k] += 1

    jold = None
    for j in arr[1:-1]:
        i = int(j/r)
        k = int(j*r)
        cnt += left[i] * right[k]

        left[j] += 1
        if jold is not None:
            right[j] -= 1
        jold = j

        #print(left,right)
    return cnt
        
def countTripletsAlmost(arr, r):
    cnt = 0
    for i , e in enumerate(arr):
        leftCnt = arr[:i].count(int(e/r))
        rightCnt = arr[i+1:].count(int(e*r))
        if leftCnt > 0 and rightCnt > 0:
            cnt += leftCnt * rightCnt
    return cnt

def countTripletsZ(arr, r):
    cnt = 0
    for i , e in enumerate(arr):
        left = Counter()
        right = Counter()
        for j , l in enumerate(arr):
            if j < i:
                left[l] += 1
            else:
                right[l] += 1
        leftCnt = left[int(e/r)]
        rightCnt = right[int(e*r)]
        if leftCnt > 0 and rightCnt > 0:
            cnt += leftCnt * rightCnt
    return cnt
        
def countTripletsX(arr, r):
    cnt = 0
    d = Counter()
    for i in arr:
        d[i] += 1
    print(d)
    for j in arr:
        i = int(j/r)
        k = int(j*r)
        if i in d and k in d:
            cnt += d[i] + d[k]
            #cnt += max(d[i],d[k])
            #cnt += d[k]
    return cnt
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

