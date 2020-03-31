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
    current_frequency = missiles[0][1]
    current_time = missiles[0][0]
    hackerX_missile = [current_frequency]

    for frequencies in missiles:
        # Remainder of frequencies and current_frequency / 2 = #hackerX_missiles
        frequency_checker = abs(current_frequency - frequencies[1])
        print("\nFrequency A is currently ", frequencies[1]," , while frequency B is currently ", current_frequency,
              "\nDifference between fA and fB is: ", frequency_checker)

        if frequency_checker > 1 and current_time != frequencies[0]:
            # Add the amount of hackerX missiles based on the number of times country A's frequency can be divided by 2
            hackerX_missile.append(frequencies[1])

        current_time = frequencies[0]
        current_frequency = frequencies[1]

    # Remove duplicate frequencies stored in hackerX missile systems
    hackerX_missile = list(dict.fromkeys((hackerX_missile)))

    return len(hackerX_missile)

if __name__ == '__main__':
    n = int(input())

    missiles = []

    for _ in range(n):
        missiles.append(list(map(int, input().rstrip().split())))

    result = missileDefend(missiles)

    print("\n",str(result))