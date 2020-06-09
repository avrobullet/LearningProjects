# In short, having an interface restricts you to ONLY use rules specified  in the interface
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        pass
        sum_n = 0
        for i in range(1,n+1):
            if n%i == 0:
                sum_n += i
                print("At",i,"the sum is:",sum_n)
        return sum_n

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)