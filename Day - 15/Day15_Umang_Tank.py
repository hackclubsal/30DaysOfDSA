
class interSectionofArray:
    def __init__(self,arr1,arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def intersection(self):
        arr3 = []
        for i in self.arr1:
            if i in self.arr2:
                arr3.append(i)
                self.arr2.remove(i)

        return arr3

if __name__ == "__main__":
    arr1 = [1, 3, 4, 5, 5, 6, 6, 7] 
    arr2 = [2, 5, 6, 6, 7, 8]
    obj = interSectionofArray(arr1,arr2)
    print(obj.intersection())