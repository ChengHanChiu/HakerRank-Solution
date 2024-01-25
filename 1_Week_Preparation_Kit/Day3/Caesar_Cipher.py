#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    """ 
    # misunderstanding the question
    code = []
    for i in range(len(s)):
        i += k
        if i >= len(s):
            i %= len(s)
        code.append(s[i])
    return "".join(code)
    """
    result = ''
    for char in s:
        ascii_code = ord(char)
        if ord('A') <= ascii_code and ascii_code <= ord('Z'):
            ascii_code += k
            if ascii_code > ord('Z'):
                ascii_code = ord('A') + (ascii_code - ord('A')) % 26
        elif ord('a') <= ascii_code and ascii_code <= ord('z'):
            ascii_code += k
            if ascii_code > ord('z'):
                ascii_code = ord('a') + (ascii_code - ord('a')) % 26
        result += chr(ascii_code)

    return result
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()
    s= '1X7T4VrCs23k4vv08D6yQ3S19G4rVP188M9ahuxB6j1tMGZs1m10ey7eUj62WV2exLT4C83zl7Q80M'
    s='Always-Look-on-the-Bright-Side-of-Life'
    # k = int(input().strip())
    k= 27
    k= 5

    result = caesarCipher(s, k)


    print(result)

    # fptr.write(result + '\n')

    # fptr.close()

    '''
    test case0
    >>11
    >>middle-Outz
    >>2
    okffng-Qwvb
    '''
    '''
    test case1
    >>38
    >>Always-Look-on-the-Bright-Side-of-Life
    >>5
    Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj
    '''