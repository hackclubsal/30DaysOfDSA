# Day 2: Rotate array by k times

class rotateTheArray():
    def __init__(self,k,arr):
        self.k = k
        self.arr = arr

    def rotate(self):
        for i in range(self.k):
            self.arr = [self.arr[-1]] + self.arr[0:-1]

    def printArray(self):
        print(self.arr)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7] 
    k = 3
    obj = rotateTheArray(k,arr)
    obj.rotate()
    obj.printArray()