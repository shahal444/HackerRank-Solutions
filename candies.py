#!/bin/python3

import math
import os
import random
import re
import sys

def candies(n, arr):
    # Write your code here
    # Initialize an array of the same length as 'arr' with all elements set to 1
    candies = [1] * n

    # Traverse 'arr' from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candies[i] = candies[i - 1] + 1

    total_candies = candies[-1]

    # Traverse 'arr' from right to left and update 'candies'
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = candies[i + 1] + 1

        total_candies += candies[i]

    return total_candies
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()