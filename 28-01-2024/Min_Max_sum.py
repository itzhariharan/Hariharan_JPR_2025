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
    # Write your code here
    sum = 0
    min = max = arr[0]
    for i in arr:
      sum = sum + i
      if i < min:
        min = i
      if i > max:
        max = i

    print(sum-max, sum - min)
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
