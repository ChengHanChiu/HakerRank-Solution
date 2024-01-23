#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    counter = {}
    for i in a:
        if i in counter:
            counter[i]+=1
        else:
            counter[i] = 1
    for k, v in counter.items():
        if v ==1:
            return k

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()

'''
test case0
>>1
>>1
1
'''
'''
test case1
>>3
>>1 1 2
2
'''
'''
test case2
>>5
>>0 0 1 2 1
2
'''