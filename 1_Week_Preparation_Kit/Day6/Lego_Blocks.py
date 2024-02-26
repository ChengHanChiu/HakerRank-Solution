#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
'''
def legoBlocks(n, m): # only for work
    # Write your code here
    ceil = 10**9+7
    r = [0]*(m+1)
    a = [0]*(m+1)

    a[0] = 1
    for j in range(1, m+1):
        a[j] += a[j-1] if j-1>=0 else 0
        a[j] += a[j-2] if j-2>=0 else 0
        a[j] += a[j-3] if j-3>=0 else 0
        a[j] += a[j-4] if j-4>=0 else 0
    for j in range(1, m+1):
        a[j] = a[j] % ceil
        a[j] = a[j] ** n
        a[j] = a[j] % ceil
    
    r[1] = 1
    for j in range(2, m+1):
        r[j] = a[j]
        for k in range(1, j):
            r[j] -= r[k]*a[j-k]
        r[j] = r[j] % ceil
    return r[m]%ceil
'''
def legoBlocks(n, m):
    # Write your code here
    M = 1000000007

    a = [0,1,2,4,8] # a[i] is the number of all walls with width i 
    for j in range(5,m+1):  # this formula executes only when we have width 5 or more
        a.append((a[j-1]+a[j-2]+a[j-3]+a[j-4])%M)
    
    for i in range(m+1): # this will give us all the walls for height n 
        a[i] = pow(a[i],n,M)

    # let r[i] be the number of good layouts that have height n, and width i
    r = [a[i] for i in range(m+1)] # start with all of them 
    for i in range(1,m+1):
        for j in range(1,i):
            r[i] -= (r[j]*a[i-j]) # subtract the number of bad layouts, when the FIRST vertical break in the wall appears at index j 
        r[i] = r[i]%M # make the computations easier 
    return r[m]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        # fptr.write(str(result) + '\n')
        print(result)

    # fptr.close()
