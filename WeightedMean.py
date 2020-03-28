# Enter your code here. Read input from STDIN. Print output to STDOUT
array_x = []
array_w = []

# Array length
array_length = float(input())
# Array elements
array_elements = input()
array_elements = array_elements.split()
# Array weighted elements
weighted_elements = input()
weighted_elements = weighted_elements.split()

# Amount of elements placed in array
for element in array_elements:
    array_x.append(float(element))
for element in weighted_elements:
    array_w.append(float(element))

# Calculate the weighted mean
z = 0
weighted_sum = []
while z < array_length:
    weighted_sum.append(array_x[z] * array_w[z])
    z+=1

sum_num = sum(weighted_sum)
sum_denom = sum(array_w)

weighted_mean = sum_num/sum_denom
weighted_mean = round(weighted_mean, 1)
print(weighted_mean)

# Add array length to the front of the list once all the calculations have been completed
array_x.insert(0,array_length)