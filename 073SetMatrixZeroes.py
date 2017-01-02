class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        rows, cols = [], []
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)

        for cur_row in rows:
            for j in range(col):
                matrix[cur_row][j] = 0

        for cur_col in cols:
            for j in range(row):
                matrix[j][cur_col] = 0

        return matrix

B = [[1,0,5,7],[10,11,16,20],[23,30,34,50]]
c = Solution()
print(c.setZeroes(B))
