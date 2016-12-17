class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        matrix.reverse()
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(i+1, col):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return
