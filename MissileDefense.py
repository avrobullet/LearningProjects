#!/bin/python3
import os
import sys

#
# Complete the missileDefend function below.
#
def missileDefend(missiles):
    #
    # Write your code here.
    #
    hackerX_missile = 1

    for frequencies in missiles:
        # Remainder of frequencies and current_frequency / 2 = #hackerX_missiles
        if frequencies[1]//2 >= 2:
            hackerX_missile += 1

    return hackerX_missile

if __name__ == '__main__':
    n = int(input())

    missiles = []

    for _ in range(n):
        missiles.append(list(map(int, input().rstrip().split())))

    result = missileDefend(missiles)

    print(str(result))