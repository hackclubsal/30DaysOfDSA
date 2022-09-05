## Given a sorted list of numbers in which all elements appear twice except one element that appears only once, find the number that appears only once.

# Example:
# 1, 1, 2, 3, 3, 4, 4
# Here, ‘2’ appears once and all other elements appear twice.

# - Input: ([1, 1, 2, 3, 3, 4, 4])  
#      =>it’s 2
# - Output:2

class numberAppearOnce:
    def __init__(self, arr):
        self.arr = arr

    def findNumber(self):
        for i in range(len(self.arr)):
            if self.arr.count(self.arr[i]) == 1:
                return self.arr[i]

if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 4, 4]
    obj = numberAppearOnce(arr)
    print(obj.findNumber())
