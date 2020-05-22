import math
import time

class PrimeChecker():
    def isPrime(self,n):
        if n == 1:
            return "Prime"
        if n == 2:
            return "Prime"
        if n > 2 and n%2==0:
            return "Prime"

        max_divisor = math.floor(math.sqrt(n))
        print(n,max_divisor)
        for i in range(3, 1+max_divisor, 2):
            if n % i == 0:
                return "Not prime"
            else:
                return "Prime"

pr_validate = PrimeChecker()
t = int(input())
for n in range(1,t):
    t0 = time.time()
    print(n, pr_validate.isPrime(n))
    t1 = time.time()
    #print(t1 - t0)
#primes = []
#for iteration in range(t): primes.append(int(input()))
#for iteration in range(t):
#    t0 = time.time()
#    print(primes[iteration], pr_validate.isPrime(primes[iteration]))
#    t1 = time.time()
#    print(t1 - t0)

