#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    cnt_pos, cnt_neg, cnt_zero = 0, 0, 0
    for i in arr:
        if i > 0:
            cnt_pos+=1
        elif i < 0:
            cnt_neg+=1
        else:
            cnt_zero+=1
    total = cnt_pos+cnt_neg+cnt_zero
    print(f"{round(cnt_pos/total, 6):.6f}")
    print(f"{round(cnt_neg/total, 6):.6f}")
    print(f"{round(cnt_zero/total, 6):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

'''
test case0
>>6
>>-4 3 -9 0 4 1
0.500000
0.333333
0.166667
'''

'''
test case1
>>8
>>1 2 3 -1 -2 -3 0 0
0.375000
0.375000
0.250000
'''
