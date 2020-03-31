# !/bin/python3

import math
import os
import random
import re
import sys

# variables
ar_matching = []
ar_notmatching = []
pairs_found = 0
pairs_total = 0
accept_pairs = False

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    global ar_matching
    global ar_notmatching
    global pairs_found
    global pairs_total
    global accept_pairs

    # Sort the 1D list "ar" to match all of the socks
    ar.sort()

    # Create a 2D list "ar_matching" of paired socks amount
    while ar:
        # Next sock
        sock = ar[0]

        # Counts the amount of each sock type
        sock_amount = ar.count(sock)
        print(ar_notmatching)
        print(ar_matching)
        print(ar)
        # Continue checking the next number
        input_user = input("Next value? (y/n)")
        if input_user == "y":
            print("Checking ", sock," for pairs...")
            if sock_amount % 2 == 0 and sock_amount > 1:
                # ar_matching[sock-1].append(sock, sock_amount)
                pairs_found = sock_amount / 2
                print(sock, " has ", sock_amount / 2, " pair(s)!")
                accept_pairs = True
            elif sock_amount % 2 == 1 and sock_amount > 1:
                pairs_found = (sock_amount - 1) / 2
                print(sock, " has ", (sock_amount - 1) / 2, " pair(s)!")
                accept_pairs = True
            # All socks without a single matching pair are moved
            else:
                print("Placing ", sock, " away...")
                ar_notmatching.append(sock)

            # Tally sock pairs
            if accept_pairs:
                sock_pairs = [sock, pairs_found]
                ar_matching.append(sock_pairs)

            # Remove the paired socks
            while (sock_amount):
                try:
                    ar.remove(sock)
                    sock_amount -= 1
                except ValueError:
                    print("No more socks to check!")

            # Revert pair checker to prevent unwanted socks without pairs to be wanted
            accept_pairs = False
        else:
            print("Skipping...")

    # Return sock pairs found in stored
    for pairs in ar_matching:
        pairs_total += pairs[1]

    return int(pairs_total)

if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)

