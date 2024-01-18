#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    t = datetime.strptime(s, '%I:%M:%S%p')
    t = t.strftime('%H:%M:%S')
    return t
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')

    # fptr.close()

'''
test case0
>>07:05:45PM
19:05:45
'''
'''
test case1
>>12:40:22AM
00:40:22
'''
'''
test case2
>>06:40:03AM
06:40:03
'''
'''
test case3
>>12:05:39AM
00:05:39
'''
'''
test case4
>>12:45:54PM
12:45:54
'''
'''
test case5
>>02:34:50PM
14:34:50
'''
'''
test case6
>>04:59:59AM
04:59:59
'''
'''
test case7
>>04:59:59PM
16:59:59
'''
'''
test case8
>>12:00:00AM
00:00:00
'''
'''
test case9
>>11:59:59PM
23:59:59
'''