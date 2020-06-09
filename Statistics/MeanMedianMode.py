# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as stats
array_x = []

# Array length
array_length = float(input())
# Array elements
array_elements = input()
array_elements = array_elements.split()

# Amount of elements placed in array
for element in array_elements:
    array_x.append(float(element))

# Sort array in increasing order
array_x.sort()

# Get the mean from the array
mean_value = round(stats.mean(array_x), 1)
print(mean_value)

# Get the median from the array
median_value = round(stats.median(array_x), 1)
print(median_value)

element_mode = 0
element_mode_present = False

x = 0
try:
    while x < len(array_x):
        if array_x[x] == array_x[x+1]:
            element_mode = array_x[x]
            print(element_mode)
            element_mode_present = True
            break
        x += 1
except IndexError:
    # If no mode is found then print the smallest element of the list
    if element_mode_present == False:
        print(int((array_x[0])))

# Add array length to the front of the list once all the calculations have been completed
array_x.insert(0,array_length)