#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    # Create dictionaries to store the counts of numbers in arr and brr
    count_arr = {}
    count_brr = {}
    
    # Populate count_arr with counts from arr
    for num in arr:
        if num in count_arr:
            count_arr[num] += 1
        else:
            count_arr[num] = 1
    
    # Populate count_brr with counts from brr
    for num in brr:
        if num in count_brr:
            count_brr[num] += 1
        else:
            count_brr[num] = 1
    
    # Initialize a list to store the missing numbers
    missing_numbers = []
    
    # Compare the counts in arr and brr to find missing numbers
    for num, count in count_brr.items():
        if num not in count_arr or count_arr[num] < count:
            missing_numbers.append(num)
    
    return sorted(missing_numbers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
