#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
'''
def minimumBribes(q): 
    # Write your code here
    bribes = 0
    for i in range(len(q)-1,0 ,-1):
        if q[i]==i+1:
            pass
        elif q[i-1]==i+1:
            q[i], q[i-1] = q[i-1], q[i]
            bribes+=1
        elif q[i-2]==i+1:
            q[i-1], q[i-2] = q[i-2], q[i-1]
            q[i], q[i-1] = q[i-1],  q[i]
            bribes +=2
        else:
            return 'Too chaotic'
    return bribes
'''
def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i in range(len(q)-1, 0, -1):
        org = i+1
        if q[i] < org:
            if q[i-2] == org:
                q[i-1], q[i-2] = q[i-2], q[i-1]
                q[i], q[i-1] = q[i-1],  q[i]
                bribes += 2
            elif q[i-1] == org:
                q[i], q[i-1] = q[i-1],  q[i]
                bribes += 1
            else:
                return 'Too chaotic'
    return bribes
'''
# bubble sort method
def minimumBribes(q):
    # Write your code here
    bribes = 0
    q_sorted = sorted(q)
    while q != q_sorted:
        for i in range(len(q)-1):
            if q[i] - (i + 1) >2:
                return 'Too chaotic'
            if q[i] > q[i+1]:
                q[i], q[i+1] = q[i+1], q[i]
                bribes += 1
                
    return bribes
'''


if __name__ == '__main__':
    # t = int(input().strip())
    t = 1

    for t_itr in range(t):
        # n = int(input().strip())
        n=8

        # q = list(map(int, input().rstrip().split()))
        q = [1, 2, 5, 3, 7, 8, 6, 4]

        print(minimumBribes(q))
