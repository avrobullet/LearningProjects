#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    val = 0
    valley = 0
    for char in s:
        if char == 'D': val -=1
        else: val +=1

        if val == 0 and char == 'U': valley+=1
    return valley

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)