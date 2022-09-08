# Q8) Given an integer array N, find the contiguous subarray which has the largest sum and return its sum.
# Input: N = [-2, -3, 4, -1, -2, 1, 5, -3]

"""
Example-1: 
- Input: N = [-2,1,-3,4,-1,2,1,-5,4]
- Output: 6

Example-2:
- Input: N= [5,4,-1,7,8]
- Output: 23
"""


class MaxSubArray:
    def __init__(self, array):
        self.array = array
        self.max_sum = 0
        self.max_subarray = []

    def subarray(self):
        for i in range(len(self.array)):
            for j in range(i, len(self.array)):
                print(self.array[i:j+1])
                if sum(self.array[i:j+1]) > self.max_sum:
                    self.max_sum = sum(self.array[i:j+1])

        return self.max_sum

if __name__ == "__main__":
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    max_subarray = MaxSubArray(array)
    print(max_subarray.subarray())
