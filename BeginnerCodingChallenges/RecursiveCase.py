class MyMath():
    # Inform user of this class's functionality
    def __init__(self):
        print("Existing functionality: \n",
              "Select multiplication by typing 'X Y multiplication'\n",
              "Select exponent by typing 'X Y exponent'\n",
              "Select factorial by typing 'X factorial'\n")
        self.a = "hi"

    # Run function based on input
    def run(self, n, k, choice):
        if isinstance(n, int) and isinstance(k, int) and choice == "multiplication":
            print(self.recursiveMultiplication(n, k))
        elif isinstance(n, int) and isinstance(k, int) and choice == "exponent":
            print(self.recursiveExponent(n, k))
        elif isinstance(n, int) and k is None and choice == "factorial":
            print(self.recursiveFactorial(n))
        else:
            print("Improper values")

    # Recursively add the base case of k based on n
    def recursiveMultiplication(self, n, p):
        if p > 1:
            return n * self.recursiveMultiplication(n, p - 1)
        elif p == 1:
            return n
        elif p == 0:
            return 1
    # Find the exponential value the base case of k based on n
    def recursiveExponent(self, n,k):
        if n > 1:
            return k * self.recursiveExponent(n-1, k)
        elif n == 1:
            return k
    # Find the factorial the base case of k based on n
    def recursiveFactorial(self, n):
        if n > 1:
            return n * self.recursiveFactorial(n-1)
        elif n == 1:
            return n
# Start application
def main():
    mymath = MyMath()
    n,k,mathchoice = list(map(str, input().rstrip().split()))
    mymath.run(int(n), int(k), mathchoice)
# Find main to begin
if __name__ == "__main__":
    mymath = MyMath()
    main()
