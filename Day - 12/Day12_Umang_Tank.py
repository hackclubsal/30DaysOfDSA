
class DistinctElement:
    def __init__(self, arr,k):
        self.arr = arr
        self.k = k

    def distinct(self):
        lis = []
        for i in range(len(self.arr) - self.k+1):
            lis.append(self.arr[i:i+self.k])

        for i in range(len(lis)):
            print(len(set(lis[i])), end=" ")




if __name__ == "__main__":
    arr = [1, 2, 1, 3, 4, 2, 3]
    k = 4
    obj = DistinctElement(arr,k)
    obj.distinct()