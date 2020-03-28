# This is another way...
# n = int(input())
# x = sorted(map(int, input().split()))
# print(x)
# from statistics import median
# print(int(median(x[:n//2])))
# print(int(median(x)))
# print(int(median(x[(n+1)//2:])))

# Enter your code here. Read input from STDIN. Print output to STDOUT
counter = 2
quartile_medians = []

# Input array length and elements
array_elements = int(input())
array_q1 = sorted(map(int, input().split()))

# Set array length
array_length = len(array_q1)

# Sort array
array_q1.sort()
print(array_q1)

def quartiles(array):
    global counter
    global quartile_medians

    # array has even length
    if len(array) % 2 == 0:
        array_q2 = array[:(len(array)//2)-1]
        array_q3 = array[(len(array)//2):]
        q_value = array[(len(array)//2)-1] + array[(len(array)//2)]
        q_value = int(q_value/2)
        print(q_value, " even")
        quartile_medians.append(q_value)

    # array has odd length
    elif len(array) % 2 == 1:
        array_q2 = array[:len(array)//2]
        array_q3 = array[len(array)//2+1:]
        print(array[len(array)//2], " odd")
        quartile_medians.append(array[len(array)//2])
    # Decrement counter
    counter -= 1

    # Break cycle
    if counter > 0:
        print(array_q2, " || ", array_q3, " || counter: ", counter)
        return quartiles(array_q2), quartiles(array_q3)

# Show into quartiles
quartiles(array_q1)

# Sort and show quartile medians found
quartile_medians.sort()
for elements in quartile_medians:
    print(elements)