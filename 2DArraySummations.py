#!/bin/python3
import math
import os
import random
import re
import sys

# arr[r][c]
def hourglassSum():
    global c,r,arr, max_hourglass_sum
    hourglass_sum = 0

    print("\nCurrently at column: ", c,
          "\nCurrently at row: ", r)
    # Calculate the sum of a 3x3 matrix within the specified boundaries of 'r' and 'c' in array 'arr'
    for i in range(r, r+3):
        for j in range(c, c+3):
            # Determine the hourglass matrix style from the array where i == 1 and j == 0 or 2 are not computed
            try:
                if i != 1 and j != 0 or j != 2:
                    hourglass_sum += arr[i+r][j+c]
            except IndexError:
                print("Breaking...")
                break
    # Only keep the highest sum found
    print(hourglass_sum)
    if max_hourglass_sum <= hourglass_sum:
        max_hourglass_sum = hourglass_sum
    # Redefine the next column coordinates for the 3x3 matrix boundaries based on 'c'
    if c <= len(arr[0])-3 and r <= len(arr)-3:
        print("Going again!")
        c += 1
        # # Redefine the next row coordinates for the 3x3 matrix boundaries based on 'r'
        if c == len(arr[0])-3 and len(arr) > 3 and len(arr)%3 == 0:
            r += 3
        hourglassSum()
    else:
        print("Done!")

max_hourglass_sum = 0
c = 0
r = 0

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print("Array's row: ",len(arr),
          "\nArray's column: ",len(arr[0]))
    hourglassSum()
    print(max_hourglass_sum)