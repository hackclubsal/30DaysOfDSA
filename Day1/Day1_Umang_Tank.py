# Day 1: Binary sorted Array in Linear Time

class binarySortedArray:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.count = 0

    def BinarySortedArray(self):
        for i in range(self.n):
            if self.arr[i] == 0:
                self.count += 1
        for i in range(self.count):
            self.arr[i] = 0
        for i in range(self.count, self.n):
            self.arr[i] = 1

    def printArray(self):
        print(self.arr)

if __name__ == "__main__":
    arr = [1, 0, 1, 0, 1, 0, 0, 1]
    obj = binarySortedArray(arr)
    obj.BinarySortedArray()
    obj.printArray()