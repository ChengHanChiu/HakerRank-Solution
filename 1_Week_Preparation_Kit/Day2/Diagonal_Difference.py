#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
 
""" 
# solution1
def diagonalDifference(arr):
    d1, d2 = 0, 0
    row = len(arr)-1
    col = len(arr[0])-1
    row_cnt, col_cnt = 0, 0
    while row_cnt!=row+1 and col_cnt!= col+1:
        
        d1+=arr[row_cnt][col_cnt]
        d2+=arr[row-row_cnt][col_cnt]

        row_cnt+=1
        col_cnt+=1

    return abs(d1-d2)
"""
def diagonalDifference(arr):
    d1, d2 = 0, 0
    n = len(arr)
    for i in range(n):
        d1+=arr[i][i]
        d2+=arr[n-1-i][i]

    return abs(d1-d2)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # arr = []

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

'''
test case0
>>3
>>11 2 4
>>4 5 6
>>10 8 -12
15
'''
'''
test case1
>>4
>>-1 1 -7 -8
>>-10 -8 -5 -2
>>0 9 7 -1
>>4 4 -2 1
1
'''
