class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.sums = []
        else:
            row, col = len(matrix), len(matrix[0])
            self.sums = [[0] * (col+1) for _ in range(row+1)]
            for i in range(1, row+1):
                for j in range(1, col+1):
                    self.sums[i][j] = self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        if not self.sums:
            return 0

        r1, c1 = row1+1, col1+1
        r2, c2 = row2+1, col2+1
        return self.sums[r2][c2] + self.sums[r1-1][c1-1] - self.sums[r2][c1-1] - self.sums[r1-1][c2]

# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))
print(numMatrix.sumRegion(1, 1, 2, 2))
print(numMatrix.sumRegion(1, 2, 2, 4))
