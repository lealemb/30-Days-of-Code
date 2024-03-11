class Difference:
    def __init__(self, a):
        self.__elements = a

        self.maximumDifference = 0

    def computeDifference(self):
        n = len(self.__elements)
        for i in range(n):
            for j in range(i + 1, n):
                absolute_diff = abs(self.__elements[i] - self.__elements[j])
                if absolute_diff > self.maximumDifference:
                    self.maximumDifference = absolute_diff

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
