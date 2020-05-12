import math, time

class Prime():
    def __init__(self):
        self.counter = 0
    def test(self,n):
        if n==1: return "Not prime"
        if n == 2: return "Prime"

        floor_divisor = math.floor(math.sqrt(n))
        for i in range(2,floor_divisor+1):
            #print(n,i,floor_divisor)
            if n%i == 0:
                return "Not prime"
        return "Prime"

    def isPrime(self,n):
        temp_counter = 0
        if n == 1:
            return "Prime"
        # Every number n can be divided into a an equal set of fractions that are inverse of each other, yielding the
        # same results. So to cut calculation time down, just iterate to the last fraction before the inverse set begins.
        # That last fraction just so happens to the square root of n: sqrt(n)*sqrt(n) = n
        max_divisor = math.floor(math.sqrt(n))
        for i in range(2,n+1):
            if n%i == 0:
                temp_counter += 1
            if i == n:
                self.counter = temp_counter
                temp_counter = 0
        # If determined counts for when n can only be divisible
        return "Prime" if self.counter == 1 else "Not prime"


t = int(input())
prime = Prime()
primes = []
for values in range(t): primes.append(int(input()))
for i in range(len(primes)):
    t0 = time.time()
    #print(primes[i], prime.isPrime(primes[i]))
    print(primes[i], prime.test(primes[i]))
    t1 = time.time()