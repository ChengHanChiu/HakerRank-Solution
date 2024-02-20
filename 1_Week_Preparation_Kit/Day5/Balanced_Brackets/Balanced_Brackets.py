#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
bracket_dict = {'(':')', '{':'}', '[':']'}

def isBalanced(s):
    # Write your code here
    if len(s) %2 !=0: return 'NO'
    # mid = len(s)//2
    stack = []
    for i in range(len(s)):
        if s[i] in bracket_dict.keys():
            stack.append(bracket_dict[s[i]]) 
        else:
            if len(stack) == 0:
                return 'NO'
            if s[i] != stack.pop():
                return 'NO'
    if len(stack) > 0:
        return 'NO'
    return 'YES'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())
    t = 3

    for t_itr in range(t):
        # s = input()
        s = '{[()]}'
        # s =  '{[(])}' 
        # s = '{{[[(())]]}}'
        # s = '{{)[](}}'
        s = '}([[{)[]))]{){}['

        result = isBalanced(s)

        # fptr.write(result + '\n')
        print(result)

    # fptr.close()
