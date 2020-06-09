class Calculator():
    # Calculate 'n' to the power of 'p'
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            if p > 1:
                return n * self.power(n,p-1)
            elif p == 1:
                return n
            elif p == 0:
                return 1

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)