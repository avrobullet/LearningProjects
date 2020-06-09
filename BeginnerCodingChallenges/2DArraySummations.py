#!/bin/python3
import math
import os
import random
import re
import sys
# FML this would have been MUCH better:
#res = []
#for i in range(0,4):
#	for j in range(0,4):
#		s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
#		res.append(s)
#print(max(res))

# Hourglass matrix shape validation using counter for iterating and confirming appropriate arr[][] to add
# a = 0; b = 1; c = 2
# - = 3; d = 4; - = 5
# e = 6; f = 7; g = 8
def matrixShape(counter):
    if counter == 3 or counter == 5:
        return False
    else:
        return True

# Find the max value of any hourglass matrix found
def maxValueFound(hourglass_sum):
    global max_hourglass_sum
    # Set first value found to be set as the max_hourglass_sum
    if not max_hourglass_sum:
        max_hourglass_sum.append(hourglass_sum)
    #Compare the previous and current supposed "max" values and determine which one is larger
    elif max_hourglass_sum:
        if max_hourglass_sum[0] <= hourglass_sum:
            max_hourglass_sum[0] = hourglass_sum

# arr[r][c]
def hourglassSum():
    global c,r,arr, max_hourglass_sum
    hourglass_sum = 0
    counter = 0
    print("Rows",r, "to", r+3, "; columns: ",c,"to", c+3)
    # Calculate the sum of a 3x3 matrix within the specified boundaries of 'r' and 'c' in array 'arr'
    for i in range(r, r+3):
        for j in range(c, c+3):
            # Determine the hourglass matrix style from the array
            try:
                if matrixShape(counter):
                    hourglass_sum += arr[i][j]
            except IndexError:
                break
            # Keeping track of hourglass iteration
            counter +=1
    # Only keep the highest sum found
    print(hourglass_sum)
    maxValueFound(hourglass_sum)

    # Redefine the next row coordinates for the 3x3 matrix boundaries based on 'r'
    if c == len(arr[0])-3 and r == len(arr)-3:
        print(max_hourglass_sum.pop(), "is the highest number!")
    elif c == len(arr[0])-3 and r <= len(arr)-3 and len(arr) > 3:
        r += 1
        c = 0
        hourglassSum()
    else:
        print("Going again!")
        c += 1
        hourglassSum()


max_hourglass_sum = []
c = 0
r = 0

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print("Array's row: ",len(arr),
          "\nArray's column: ",len(arr[0]))
    hourglassSum()