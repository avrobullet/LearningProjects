a = [1, 2, 3, 4, 5]
d = 4

def rotLeft(a, d):

    tempt_array = [0]*len(a)

    for i in range(len(a)):
        tempt_position = i - d
        tempt_array[tempt_position] = a[i]

    return tempt_array

print(rotLeft(a,d))