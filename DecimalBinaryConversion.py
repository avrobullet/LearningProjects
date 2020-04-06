# Determine consecutive 1's in the binary value
def consecutiveOnes(bin_number):
    bin_number = max(sorted(bin_number.split('0')))
    return len(bin_number)

# Convert decimal to binary as a list
def decimalToBinary(n):
    bin_number = ""
    while n >= 1:
        remainder = n%2
        binary_value.insert(0, str(remainder))
        bin_number += str(remainder)
        n = round(n//2)

    return bin_number

binary_value = []
#
if __name__ == '__main__':
    n = int(input())
    bin_number = decimalToBinary(n)
    print(consecutiveOnes(bin_number), bin_number)