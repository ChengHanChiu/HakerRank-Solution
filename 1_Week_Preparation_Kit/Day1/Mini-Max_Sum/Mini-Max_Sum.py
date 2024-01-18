#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # list.sort(arr)
    # min, max =0,0
    # for i in range(4):
    #     min+=arr[i]
    #     max+=arr[len(arr)-1-i]
    
    print(sum(arr)-max(arr), sum(arr)-min(arr))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

'''
test case0
>>1 2 3 4 5
10 14
'''

'''
test case1
>>7 69 2 221 8974
299 9271
'''