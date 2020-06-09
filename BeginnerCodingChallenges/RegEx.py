#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    gmail_firstnames = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        # Store first name of Gmail user when their email is identified as an Gmail account
        if re.search("@gmail.com$", emailID):
            gmail_firstnames.append(firstName)
            print(firstName)
        # Sort Gmail first names alphabetically
        gmail_firstnames.sort()
    # Print all newly sorted Gmail first names
    for name in gmail_firstnames: print(name)