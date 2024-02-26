#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
'''
# Time limit exceeded
def cookies(k, A):
    # Write your code here
    cnt = 0
    A.sort(reverse = True)
    while A[-1] < k and len(A)>1: 
        new_cookies = A.pop() + 2 * A.pop()
        if len(A)==0:
            A.append(new_cookies)
            break
        temp_stack = []
        while new_cookies > A[-1]:
            temp_stack.append(A.pop())
            if len(A)==0: break
        A.append(new_cookies)
        while len(temp_stack) > 0:
            A.append(temp_stack.pop())
        cnt += 1
        if len(A)==0: break
    if A[0] < k:
        return -1
    else:
        return cnt
'''

# heap solution
import heapq

def cookies(k, A):
    heapq.heapify(A)
    count = 0
    while A[0] < k:
        if len(A) < 2: return -1
        new_cookies = heapq.heappop(A) + 2 * heapq.heappop(A)
        heapq.heappush(A, new_cookies)
        count += 1
    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
