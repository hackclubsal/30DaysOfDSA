# BinarySearch in 2D array


class Search2D:
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])

    def search(self, target):

        # Start from top right corner
        row = 0
        col = self.col - 1

        while row < self.row and col >= 0:
            if self.matrix[row][col] == target:
                return True
            elif self.matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

if __name__ == "__main__":
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]

    target = 50
    obj = Search2D(matrix)
    print(obj.search(target))