#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    ''' 
    # not work for large n&k
    p = "".join((list(n))*k)
    length = len(list(p))
    while length > 1:
        p = str(sum(list(map(int, list(p))))) 
        length = len(list(p))
        
    return int(p)
    '''
    if len(n) == k == 1:
        return int(n)

    result = sum(map(int, list(n)))

    return superDigit(str(result*k), 1) # '9875987598759875' = '9875'*4 = 29*4
    

                                                                                                                                 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = first_multiple_input[0]
    n = '9875' 

    # k = int(first_multiple_input[1])
    k=4
    # k=100000

    result = superDigit(n, k)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
