#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n : the number of towers
#  2. INTEGER m : the height of each tower
#

def towerBreakers(n, m): # (
    # Write your code here
    if m == 1: # towers
        return 2
    elif n % 2 != 0:
        return 1
    else:
        return 2

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        # fptr.write(str(result) + '\n')

    # fptr.close()

    '''
    test case0
    >>2
    >>2 2 
    >>1 4 
    2
    1
    '''
    '''
    test case1
    >>2
    >>1 7  
    >>3 7 
    2
    1
    '''