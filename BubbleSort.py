#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
array_length = len(a)
swap_iterator = 0
while array_length:
    for i_elem in range(0,len(a)):
        try:
            if a[i_elem] > a[i_elem + 1]:
                swapped_elem = a[i_elem + 1]
                a[i_elem + 1] = a[i_elem]
                a[i_elem] = swapped_elem
                swap_iterator += 1
        except IndexError:
            break
    array_length -= 1

print("Array is sorted in",swap_iterator, "swaps.",
      "\nFirst element:", a[0],
      "\nLast element :", a[len(a)-1])