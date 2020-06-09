# This is another way...
# n = int(input())
# x = sorted(map(int, input().split()))
# print(x)
# from statistics import median
# print(int(median(x[:n//2])))
# print(int(median(x)))
# print(int(median(x[(n+1)//2:])))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

counter = 2
quartile_medians = []
array_q1 = []

# Input array length and elements
array_elements_amount = int(input())
array_elements = list(map(int, input().rstrip().split()))
array_element_occurences = list(map(int, input().rstrip().split()))

# Continue evaluating array if no element occurences have been selected
if not array_element_occurences:
    for x in range(len(array_elements)):
        array_element_occurences.append(1)

# Populate the new elements based on occurences of elements
for x in range(array_elements_amount):
    for y in range(array_element_occurences[x]):
        array_q1.append(array_elements[x])

# Sort newly populated array
array_q1.sort()
# Set array length
array_length = len(array_q1)

# Find standard deviation of array inputed
def standardDeviation():
    # Get the standard deviation from the array using numpy
    std_dev_numpy = float(numpy.std(array_q1))
    print(round(std_dev_numpy, 1))

# Find the different between q1 and q3 stored in quartile_medians
def interquartiles():
    global quartile_medians

    # Sort and show quartile medians found
    quartile_medians.sort()
    # Calculate the interquartile
    interquartile_difference = float(abs(quartile_medians[0]
                                   -quartile_medians[len(quartile_medians)-1]))
    print(interquartile_difference)

def quartiles(array):
    global counter
    global quartile_medians

    # array has even length
    if len(array) % 2 == 0:
        array_q2 = array[:(len(array)//2)]
        array_q3 = array[(len(array)//2):]
        q_value = array[(len(array)//2)-1] + array[(len(array)//2)]
        q_value = int(q_value/2)
        #print(q_value, " even")
        quartile_medians.append(q_value)

    # array has odd length
    elif len(array) % 2 == 1:
        array_q2 = array[:len(array)//2]
        array_q3 = array[len(array)//2+1:]
        #print(array[len(array)//2], " odd")
        quartile_medians.append(array[len(array)//2])
    # Decrement counter
    counter -= 1

    # Break cycle
    if counter > 0:
        #print(array_q2, " || ", array_q3, " || counter: ", counter)
        return quartiles(array_q2), quartiles(array_q3)

# Show into quartiles
quartiles(array_q1)
interquartiles()
standardDeviation()