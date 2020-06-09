class Difference:
    # Constructor
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.biggest_num = 0
        self.lowest_num = 0

	# Add your code here
    def computeDifference(self):
        # Find biggest and lowest numbers (ele) in the array
        self.__elements.sort()
        self.biggest_num = self.__elements.pop(0)
        self.lowest_num = self.__elements.pop(len(self.__elements)-1)

        print(self.biggest_num,self.lowest_num)
        self.maximumDifference = abs(self.biggest_num - self.lowest_num)
        # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)