











import numpy

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c) == 1: return 0
    if len(c) == 2: return 0 if c[1] == 1 else 1
    if c[2] == 1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2] == 0:
        return 1 + jumpingOnClouds(c[2:])

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)